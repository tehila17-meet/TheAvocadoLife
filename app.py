import json
import time
from datetime import datetime

from flask import Flask, request, json
from flask_cors import CORS, cross_origin
import subprocess

import os
from arango_handler.arango_handler import ArangoHandler
from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument
from consts import EntryConsts, KeywordConsts, ArangoConsts, StatusConsts
from entries.entries_database import Entry, session
from utils import check_arango_connectivity, remove_sent_entries

app = Flask(__name__)
cors = CORS(app)
main_arango_handler = ArangoHandler()
arango_exe_path = "arango_server\\usr\\bin\\arangod.exe"
arango_process = subprocess.Popen([arango_exe_path])


@app.route("/")
def is_arango_connected():
    arango_connectivity_status = check_arango_connectivity(main_arango_handler)
    return ArangoConsts.ARANGO_CONNECTION_SUCCESS_MSG if arango_connectivity_status == 1 else arango_connectivity_status



@app.route("/get_document_names/<string:collection_name>", methods=["GET", "POST"])
@cross_origin()
def get_document_names(collection_name: str):
    all_documents = main_arango_handler.handle_getter(ArangoConsts.DOCUMENTS_KEYWORD, collection_name)
    return json.dumps(
        {KeywordConsts.RESULT_KEYWORD: [document.title if document.title else document._key for document in
                                        all_documents]})


@app.route("/get_collection_names/<string:must_include>")
def get_collection_names(must_include: str):
    return {KeywordConsts.RESULT_KEYWORD: list(
        main_arango_handler.handle_getter(ArangoConsts.COLLECTION_KEYWORD, must_include))}


@app.route("/save_entries_locally", methods=['GET', 'POST'])
@cross_origin()
def save_entries_locally():
    entry_data = json.loads(request.data)

    new_entry = Entry(title=entry_data.get(EntryConsts.ENTRY_TITLE_KEY),
                      affectingCollection=f"Affecting-{entry_data.get(EntryConsts.AFFECTING_COLLECTION_KEY)}",
                      impactRating=entry_data.get(EntryConsts.IMPACT_RATING_KEY),
                      definingTraits=EntryConsts.DEFINING_TRAITS_DELIMITER.join(
                          entry_data.get(EntryConsts.DEFINING_TRAITS_KEY)),
                      insertionTime=datetime.today(),
                      sentToDestination=EntryConsts.NOT_SENT_DESTINATION_STATUS)

    session.add(new_entry)
    session.commit()
    return StatusConsts.ADDED_NEW_ENTRY


@app.route("/add_entries", methods=['GET', 'POST'])
@cross_origin()
def add_entries():
    if is_arango_connected() == ArangoConsts.ARANGO_CONNECTION_SUCCESS_MSG:
        new_entries = session.query(Entry).filter_by(sentToDestination=EntryConsts.NOT_SENT_DESTINATION_STATUS).all()
        for entry in list(new_entries):
            prep_document_obj = ArangoPrepDocument(affecting_collection=entry.affectingCollection, title=entry.title,
                                                   impact_rating=entry.impactRating,
                                                   insertion_time=entry.insertionTime,
                                                   defining_traits=str(entry.definingTraits).split(
                                                       EntryConsts.DEFINING_TRAITS_DELIMITER))
            print(prep_document_obj.__dict__, " prep")
            main_arango_handler.handle_creation(ArangoConsts.ENTRY_CREATION_TYPE, prep_document_obj)

            entry.sentToDestination = EntryConsts.SENT_TO_DESTINATION_STATUS
            session.commit()
        remove_sent_entries(session, Entry)
        return StatusConsts.SENT_TO_ARANGO
    return ArangoConsts.ARANGO_CONNECTION_ERROR


if __name__ == '__main__':
    app.run(host="0.0.0.0")
