from datetime import datetime
import json
from consts import SystemConsts, EntryConsts, ApiConsts
import shutil
import os
from typing import List

def get_document_with_date(document_data: dict) -> dict:
    document_data[ApiConsts.INSERTION_DATE_KEY] = datetime.today()
    return document_data

def read_file_data(file_path: str) -> dict:
    with open(file_path, "r") as entry_data_file:
        return json.loads(entry_data_file.read())

def move_entry_to_backup(file_name: str, full_path):
    shutil.move(full_path, os.getcwd() +SystemConsts.BACKUP_ENTRIES_DIR+file_name)

def remove_added_entries(session, db_name: str) -> None:
    added_entries = session.query(db_name).filter_by(sentToDestination = EntryConsts.SENT_TO_DESTINATION_STATUS).all()
    for added_entry in added_entries:
        session.delete(added_entry)
        session.commit()

def listify_data(data: str) -> List:
    return str(data).split()