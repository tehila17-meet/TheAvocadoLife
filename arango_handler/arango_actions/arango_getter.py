from pyArango import collection

from arango_handler.consts import ArangoErrorMessages
from arango_handler.queries import ArangoQueries
from cache.cache_handler import CacheHandler
from cache.consts import CacheConsts


class ArangoGetter:
    @staticmethod
    def get_collection_obj(database_object, collection_name: str) -> collection.Collection:
        collection_obj = database_object.collections.get(collection_name)
        print("COLLECTION OBJ FROM WITIHIN FUNC")
        return collection_obj if collection_obj else ArangoErrorMessages.COLLECTION_DOES_NOT_EXIST.format(
            collection_name)

    @staticmethod
    def get_document_key_by_title(document_name: str, collection_obj: collection.Collection) -> str:
        print(document_name, collection_obj)
        all_documents_in_collection = collection_obj.fetchAll()
        print(all_documents_in_collection, "ALLL DOCUMENTS")
        try:
            listified_doc_key = [document._key for document in all_documents_in_collection if
                str(document.title).lower() == str(document_name).lower()]
            print(listified_doc_key[0], "THE KEYYYY", document_name)
            return listified_doc_key[0] if listified_doc_key else None #todo: Raise or return no such doucment
        except IndexError as e:
            print(e, "jdjasofj")

    @staticmethod
    def get_collection_names(database_object, must_include: str = str()):
        if database_object == ArangoErrorMessages.ARANGO_CONNECTION_ERROR:
            cached_data = CacheHandler.get_cached_data(must_include)
            return cached_data if cached_data else str()

        else:
            collection_names = database_object.fetch_list(
                ArangoQueries.FILTERED_COLLECTION_NAMES.format(must_include=must_include))
            file_name_by_must_include = CacheConsts.CACHED_FILES_KEYWORD_MAPPING.get(must_include)
            CacheHandler.update_cached_file(file_name_by_must_include, collection_names)
            return collection_names

    @staticmethod
    def get_all_documents(database_object, collection_name: str):
        arango_collection_obj = ArangoGetter.get_collection_obj(database_object, collection_name)
        return arango_collection_obj.fetchAll()
