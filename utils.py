from datetime import datetime

def get_document_with_date(document_data: dict) -> dict:
    today = datetime.today()
    document_data["insertion_date"] = today
    return document_data