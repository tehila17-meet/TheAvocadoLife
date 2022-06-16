import pathlib

from cache.consts import CacheConsts


class CacheHandler:
    @staticmethod
    def read_cached_file(file_name):
        with open(fr"{pathlib.Path().resolve()}\{CacheConsts.BASE_CACHE_DIR}\{file_name}", "r") as cache_file:
            cache_file.readline()

    @staticmethod
    def update_cached_file(file_name, updated_data):
        with open(fr"{pathlib.Path().resolve()}\{CacheConsts.BASE_CACHE_DIR}\{file_name}", "w") as cache_file:
            cache_file.write(str(updated_data))

    @staticmethod
    def get_cached_data(must_include):
        cached_file_name = CacheConsts.CACHED_FILES_KEYWORD_MAPPING.get(must_include)
        return CacheHandler.read_cached_file(cached_file_name) if cached_file_name else None
