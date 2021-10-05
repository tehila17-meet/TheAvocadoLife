from pyArango import connection, database, collection, document, graph
from arango_handler.arango_config import ArangoConfig
from arango_handler.consts import ArangoErrorMessages, BaseCollections
from arango_handler.queries import ArangoQueries


class ArangoHandler:
    def __init__(self) -> None:
        self.connection_certificate = connection.CA_Certificate(ArangoConfig.ENCODED_CA, encoded=True)
        self.trait_arango_collection = self.get_collection_obj(BaseCollections.THE_AFFECTED_COLLECTION)
        self.caused_arango_collection = self.get_collection_obj(BaseCollections.CAUSED_COLLECTION)

    def add_new_entry(self, collection_name: str, base_document_data: dict, defining_traits: list):
        arango_collection = self.get_collection_obj(collection_name)
        new_document = arango_collection.createDocument(base_document_data)
        self.validate_and_save_doc(new_document)
        self.create_all_relationships(new_document, defining_traits)
    
    def create_new_relationship(self, new_entry: document.Document, defining_trait: str):
        defining_traits_key = self.get_trait_key_by_title(defining_trait)
        defining_traits_document = self.trait_arango_collection.fetchDocument(defining_traits_key)
        self.create_edge_link(new_entry, defining_traits_document)

    def get_trait_key_by_title(self, trait_title: str) -> str:
        all_documents = self.trait_arango_collection.fetchAll()
        return [document._key for document in all_documents if document.title == trait_title.lower() or document.title == trait_title.upper()][0]
    
    def get_collection_obj(self, collection_name: str) -> collection.Collection:
        collection_obj = self.database_object.collections.get(collection_name)
        return collection_obj if collection_obj != None else ArangoErrorMessages.COLLECTION_DOES_NOT_EXIST.format(collection_name)
    
    def get_collection_names(self, must_include: str = str()):
        return self.database_object.fetch_list(ArangoQueries.FILTERED_COLLECTION_NAMES.format(must_include=must_include))

    def create_edge_link(self, entry: document.Document, affected_document: document.Document):
        new_edge = self.caused_arango_collection.createEdge()
        new_edge.links(entry, affected_document)
        new_edge.save()

    def validate_and_save_doc(self, doc: document.Document):
        if doc.validate():
            doc.save()

    def create_all_relationships(self, doc: document.Document, all_affected_doc_names: list):
           for definig_trait in all_affected_doc_names:
            self.create_new_relationship(doc, definig_trait)

    @property
    def database_object(self, database_name: str = ArangoConfig.MAIN_DATABASE) -> database.Database:
        return self.arango_connection[database_name]

    @property
    def arango_connection(self) -> connection.Connection:
        return connection.Connection(arangoURL=ArangoConfig.ARANGO_HOST, username=ArangoConfig.USERNAME, password=ArangoConfig.PASSWORD, verify=self.connection_certificate)

