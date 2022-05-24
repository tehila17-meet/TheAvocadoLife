from pyArango import document
from arango_handler.arango_getter import ArangoGetter
from arango_handler.arango_validator import ArangoValidator

affected_collection: str
title: str
impact_rating: int
insertion_time: str
defining_traits: List[str]
dictionized_base_data: dict = {"title": title, "impact_rating": impact_rating, "insertion_time": insertion_time}
real_arango_document_object: document.Document = None

from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument

class ArangoCreator():


    @staticmethod
    def create_entry(prep_document_obj):
        arango_collection = ArangoGetter.get_collection_obj(prep_document_obj)
        new_document = arango_collection.createDocument(prep_document_obj.dictionized_base_data)
        prep_document_obj.real_arango_document_obj = new_document
        ArangoValidator.validate_and_save_doc(new_document)
        ArangoCreator.create_all_relationships(new_document, prep_document_obj.defining_traits)

    @staticmethod
    def create_relationship(arango_document_obj: document.Document, defining_trait: str):
        defining_traits_key = ArangoGetter.get_trait_key_by_title(defining_trait)
        defining_trait_collection = ArangoGetter.get_collection_obj(arango_document_obj, defining_trait)
        defining_traits_document = self.trait_arango_collection.fetchDocument(defining_traits_key)
        ArangoCreator.create_edge_link(arango_document_obj, defining_traits_document)

    @staticmethod
    def create_edge_link(arango_document_obj: document.Document, defining_trait_document: document.Document):
        new_edge = self.caused_arango_collection.createEdge()
        new_edge.links(entry, affected_document)
        new_edge.save()

    def create_all_relationships(self, arango_document_obj: document.Document, defining_traits: list):
           for defining_trait in defining_traits:
                ArangoCreator.create_relationship(arango_document_obj, defining_trait)