from pyArango import document

from arango_handler.errors.invalid_arango_entry import InvalidArangoEntry


class ArangoValidator:
    @staticmethod
    def validate_and_save_doc(real_arango_doc: document.Document):
        if real_arango_doc.validate():
            real_arango_doc.save()
        else:
            raise InvalidArangoEntry
