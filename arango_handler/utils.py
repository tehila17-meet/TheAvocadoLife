import os
from arango_handler.consts import CacheConsts



def get_full_path(file_name):
    return CacheConsts.BASE_CACHE_DIR + file_name

def read_cached_file(file_name):
    with open(os.path.join(CacheConsts.BASE_CACHE_DIR, '') + file_name, "r") as cache_file:
        print(cache_file.readline())
        cache_file.readline()


def update_cached_file(file_name, updated_data):
    with open(os.path.join(CacheConsts.BASE_CACHE_DIR, '') + file_name, "w") as cache_file:
            cache_file.write(str(updated_data))

