from pyArango import database

from arango_handler.arango_actions.arango_creator import ArangoCreator
from arango_handler.arango_actions.arango_getter import ArangoGetter
from arango_handler.arango_config import ArangoConfig
from arango_handler.arango_connector import ArangoConnector
from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument
from arango_handler.consts import ArangoErrorMessages


class ArangoHandler:
    @property
    def arango_connection(self):
        return ArangoConnector.arango_connection

    @property
    def database_object(self, database_name: str = ArangoConfig.MAIN_DATABASE) -> database.Database:
        return ArangoErrorMessages.ARANGO_CONNECTION_ERROR if self.arango_connection == ArangoErrorMessages.ARANGO_CONNECTION_ERROR else \
            self.arango_connection[database_name]

    def handle_creation(self, creation_type: str, prep_document_obj: ArangoPrepDocument):

        arango_creator = ArangoCreator(self.database_object)
        creation_mapping = {"entry": arango_creator.create_entry}
        arango_creator_func = creation_mapping.get(creation_type)
        if arango_creator_func:
            arango_creator_func(prep_document_obj)

    def handle_getter(self, get_type: str, *args):
        getter_mapping = {"documents": ArangoGetter.get_all_documents, "collections": ArangoGetter.get_collection_names}
        arango_creator_func = getter_mapping.get(get_type)
        if arango_creator_func:
            return arango_creator_func(self.database_object, args[0])
