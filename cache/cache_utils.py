from cache.consts import CacheConsts
import os

def read_cached_file(file_name):
    with open(os.path.join(CacheConsts.BASE_CACHE_DIR, '') + file_name, "r") as cache_file:
        cache_file.readline()


def update_cached_file(file_name, updated_data):
    with open(os.path.join(CacheConsts.BASE_CACHE_DIR, '') + file_name, "w") as cache_file:
            cache_file.write(str(updated_data))

def get_cached_data(must_include):
        return read_cached_file(file_name = CacheConsts.CACHED_FILES_KEYWORD_MAPPING.get(must_include))


if __name__ == '__main__':
    main()