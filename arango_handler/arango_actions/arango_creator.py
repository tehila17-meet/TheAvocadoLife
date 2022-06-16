from pyArango import document

from arango_handler.arango_actions.arango_getter import ArangoGetter
from arango_handler.arango_actions.arango_validator import ArangoValidator
from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument
from arango_handler.consts import BaseCollections


class ArangoCreator:
    def __init__(self, database_obj):
        self.database_obj = database_obj

    def create_entry(self, prep_document_obj: ArangoPrepDocument) -> None:
        affecting_collection_obj = ArangoGetter.get_collection_obj(self.database_obj,
                                                                   prep_document_obj.affecting_collection)
        new_document = affecting_collection_obj.createDocument(prep_document_obj.dictionized_base_data)
        prep_document_obj.arango_document_object = new_document
        ArangoValidator.validate_and_save_doc(new_document)
        self._create_all_relationships(prep_document_obj)

    def _create_all_relationships(self, prep_document_obj: ArangoPrepDocument):
        for defining_trait in prep_document_obj.defining_traits:
            self._create_relationship(prep_document_obj, defining_trait)

    def _create_relationship(self, prep_document_obj: ArangoPrepDocument, defining_trait: str):
        defining_trait_collection_obj = ArangoGetter.get_collection_obj(self.database_obj,
                                                                        BaseCollections.DEFINING_TRAIT_KEY)

        defining_trait_arango_key = ArangoGetter.get_document_key_by_title(defining_trait,
                                                                           defining_trait_collection_obj)
        defining_traits_document = defining_trait_collection_obj.fetchDocument(defining_trait_arango_key)
        self._create_edge_link(prep_document_obj, defining_traits_document)

    def _create_edge_link(self, prep_document_obj: ArangoPrepDocument, defining_trait_document: document.Document):
        caused_edge_collection_obj = ArangoGetter.get_collection_obj(self.database_obj,
                                                                     BaseCollections.CAUSED_EDGE_KEY)
        new_edge = caused_edge_collection_obj.createEdge()
        new_edge.links(prep_document_obj.arango_document_object, defining_trait_document)
        new_edge.save()
