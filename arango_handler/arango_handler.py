from pyArango import connection, database, collection, document, graph
from arango_handler.arango_config import ArangoConfig
from arango_handler.consts import ArangoErrorMessages, BaseCollections
from arango_handler.queries import ArangoQueries
from cache.cache_utils import read_cached_file, update_cached_file, get_cached_data
import os
from errors import InvalidArangoEntry
from arango_handler.arango_creator import ArangoCreator
from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument

class ArangoHandler:
    def __init__(self, arango_data_obj) -> None:
        #self.connection_certificate = connection.CA_Certificate(ArangoConfig.ENCODED_CA, encoded=True)
        self.defining_trait_arango = self.get_collection_obj(BaseCollections.DEFINING_TRAIT_KEY)
        self.caused_arango_collection = self.get_collection_obj(BaseCollections.CAUSED_COLLECTION)
        self.arango_data_obj = arango_data_obj


    def handle_creation(self, creation_type: str, prep_document_obj: ArangoPrepDocument):
        creation_mapping = {"entry" : ArangoCreator.create_entry, "relationship" : ArangoCreator.create_relationship,
                            "relationships" : ArangoCreator.create_all_relationships,
                            "edge_link" : ArangoCreator.create_edge_link}

        arango_creator = creation_mapping.get(creation_type)
        if arango_creator:
            arango_creator(prep_document_obj)

    def get_trait_key_by_title(self, trait_title: str) -> str:
        all_documents = self.trait_arango_collection.fetchAll()

        for docd in all_documents:
            print(docd.title, docd._key)
        return [document._key for document in all_documents if str(document.title).lower() == trait_title.lower()][0]
    
    def get_collection_obj(self, collection_name: str) -> collection.Collection:
        collection_obj = self.database_object.collections.get(collection_name)
        return collection_obj if collection_obj != None else ArangoErrorMessages.COLLECTION_DOES_NOT_EXIST.format(collection_name)
    
    def get_collection_names(self, must_include: str = str()):
        if self.database_object == ArangoErrorMessages.ARANGO_CONNECTION_ERROR:
            return get_cached_data(must_include)
        else:
            
            collection_names = self.database_object.fetch_list(ArangoQueries.FILTERED_COLLECTION_NAMES.format(must_include=must_include))
            file_name_by_must_include = CacheConsts.CACHED_FILES_KEYWORD_MAPPING.get(must_include)
            update_cached_file(file_name_by_must_include, collection_names)
            return collection_names

    def create_edge_link(self, entry: document.Document, affected_document: document.Document):
        new_edge = self.caused_arango_collection.createEdge()
        new_edge.links(entry, affected_document)
        new_edge.save()

    def validate_and_save_doc(self, doc: document.Document):
        if doc.validate():
            print("AFTER VALIDATION")
            doc.save()
        else:
            raise InvalidArangoEntry

    def create_all_relationships(self, doc: document.Document, all_affected_doc_names: list):
           for definig_trait in all_affected_doc_names:
            self.create_new_relationship(doc, definig_trait)

    @property
    def database_object(self, database_name: str = ArangoConfig.MAIN_DATABASE) -> database.Database:
        return ArangoErrorMessages.ARANGO_CONNECTION_ERROR if self.arango_connection == ArangoErrorMessages.ARANGO_CONNECTION_ERROR else self.arango_connection[database_name]

    @property
    def arango_connection(self) -> connection.Connection:
        try:
            return connection.Connection(arangoURL=ArangoConfig.ARANGO_HOST, username=ArangoConfig.USERNAME, password=ArangoConfig.PASSWORD)
        except Exception as e:
            return ArangoErrorMessages.ARANGO_CONNECTION_ERROR

    def get_cached_data(self, must_include):
        return read_cached_file(file_name = CacheConsts.CACHED_FILES_KEYWORD_MAPPING.get(must_include))
