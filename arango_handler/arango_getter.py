
from arango_handler.consts import ArangoErrorMessages
from cache.consts import CacheConsts
from pyArango import document, collection
from arango_handler.queries import ArangoQueries
from cache.cache_utils import get_cached_data, update_cached_file

class ArangoGetter():

    @staticmethod
    def get_trait_key_by_title(document_object: document.Document, trait_arango_collection: collection.Collection, trait_title: str) -> str:
        trait_title = document_object.defining_traits
        all_documents = trait_arango_collection.fetchAll()
        return [document._key for document in all_documents if str(document.title).lower() == trait_title.lower()][0]

    @staticmethod
    def get_collection_obj(database_object) -> collection.Collection:
        collection_obj = database_object.collections.get(database_object.collection_name)
        return collection_obj if collection_obj != None else ArangoErrorMessages.COLLECTION_DOES_NOT_EXIST.format(
            database_object.collection_name)

    @staticmethod
    def get_collection_names(database_object, must_include: str = str()):
        if database_object == ArangoErrorMessages.ARANGO_CONNECTION_ERROR:
            return get_cached_data(must_include)
        else:

            collection_names = database_object.fetch_list(
                ArangoQueries.FILTERED_COLLECTION_NAMES.format(must_include=must_include))
            file_name_by_must_include = CacheConsts.CACHED_FILES_KEYWORD_MAPPING.get(must_include)
            update_cached_file(file_name_by_must_include, collection_names)
            return collection_names