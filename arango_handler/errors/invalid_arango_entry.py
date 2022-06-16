
class InvalidArangoEntry(Exception):
    def __init__(self, e):
        self.message = f"Invalid Arango Entry - {e}"
        super().__init__(self.message)
