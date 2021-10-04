class ArangoQueries:
    FILTERED_COLLECTION_NAMES = """
    FOR coll in COLLECTIONS()
    FILTER LIKE(coll.name, "{must_include}%")
    RETURN coll
    """