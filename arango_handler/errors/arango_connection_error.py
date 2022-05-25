class ArangoConnectionError(Exception):
    def __init__(self, e):
        self.message = f"Connection Error - {e}"
        super().__init__(self.message)
