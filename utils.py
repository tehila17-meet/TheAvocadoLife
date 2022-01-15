from datetime import datetime
import json
from consts import SystemConsts
import shutil
import os

def get_document_with_date(document_data: dict) -> dict:
    today = datetime.today()
    document_data["insertion_date"] = today
    return document_data

def read_file_data(file_path: str) -> dict:
    with open(file_path, "r") as entry_data_file:
        return json.loads(entry_data_file.read())

def move_entry_to_backup(file_name, full_path):
    shutil.move(full_path, os.getcwd() +SystemConsts.BACKUP_ENTRIES_DIR+file_name)