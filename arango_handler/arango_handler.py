from pyArango import database

from arango_handler.arango_actions.arango_creator import ArangoCreator
from arango_handler.arango_actions.arango_getter import ArangoGetter
from arango_handler.arango_config import ArangoConfig
from arango_handler.arango_connector import ArangoConnector
from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument
from arango_handler.consts import ArangoErrorMessages, ArangoActionConsts


class ArangoHandler:
    @property
    def arango_connection(self):
        return ArangoConnector.initiate_arango_connection()

    @property
    def database_object(self, database_name: str = ArangoConfig.MAIN_DATABASE) -> database.Database:
        connection = self.arango_connection
        return ArangoErrorMessages.ARANGO_CONNECTION_ERROR if connection == ArangoErrorMessages.ARANGO_CONNECTION_ERROR else \
            connection[database_name]

    def handle_creation(self, creation_type: str, prep_document_obj: ArangoPrepDocument):
        arango_creator = ArangoCreator(self.database_object)
        creation_mapping = {ArangoActionConsts.ENTRY_CREATION_TYPE: arango_creator.create_entry}
        arango_creator_func = creation_mapping.get(creation_type)
        if arango_creator_func:
            arango_creator_func(prep_document_obj)

    def handle_getter(self, get_type: str, *args):
        getter_mapping = {ArangoActionConsts.DOCUMENT_GETTER_TYPE: ArangoGetter.get_all_documents,
                          ArangoActionConsts.COLLECTION_GETTER_TYPE: ArangoGetter.get_collection_names}
        arango_getter_func = getter_mapping.get(get_type)
        if arango_getter_func:
            return arango_getter_func(self.database_object, args[0])
