class SystemConsts:
    BASE_ENTRIES_DIR = "\\entries_holder\\"
    BACKUP_ENTRIES_DIR = "\\entry_backups\\"

class ArangoConsts:
    ARANGO_CONNECTION_ERROR = "Error Connection To Arango"
    ARANGO_CONNECTION_SUCCESS_MSG = "Welcome to the avocado life. Connection To Arango Is Established"
    
class KeywordConsts:
    RESULT_KEYWORD = "result"

class EntryConsts:
    NOT_SENT_DESTINATION_STATUS = 0
    SENT_TO_DESTINATION_STATUS = 1
    AFFECTING_COLLECTION_KEY = "affecting_collection"
    DEFINING_TRAITS_KEY = "defining_traits"
    INSERTION_DATE_KEY = "insertion_date"
    ENTRY_TITLE_KEY = "title"
    IMPACT_RATING_KEY = "impact_rating"

class StatusConsts:
    SAVED_ENTRY = "saved_entry"
    ADDED_NEW_ENTRY = "Added New Entry"
    SENT_TO_ARANGO = "Sent Entries To Arango"
