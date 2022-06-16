class ArangoErrorMessages:
    COLLECTION_DOES_NOT_EXIST = "{} - collection does not exist"
    ARANGO_CONNECTION_ERROR = "Error Connection To Arango - {error_reason}"

class BaseCollections:
    DEFINING_TRAIT_KEY = "Defining-Traits"
    CAUSED_EDGE_KEY = "Caused"

class ArangoActionConsts:
    ENTRY_CREATION_TYPE = "Entry"
    DOCUMENT_GETTER_TYPE = "documents"
    COLLECTION_GETTER_TYPE = "collections"