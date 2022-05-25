
class InvalidArangoEntry(Exception):
    def __init__(self, message):
        self.message = "Invalid Arango Entry"
        super().__init__(self.message)
