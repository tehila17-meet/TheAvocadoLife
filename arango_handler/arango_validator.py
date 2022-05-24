from errors import InvalidArangoEntry
from pyArango import document

class ArangoValidator:

    @staticmethod
    def validate_and_save_doc(real_arango_doc: document.Document):
        if real_arango_doc.validate():
            real_arango_doc.save()
        else:
            raise InvalidArangoEntry

