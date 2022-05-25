import json
from datetime import datetime

from flask import Flask, request, json
from flask_cors import CORS, cross_origin

from arango_handler.arango_handler import ArangoHandler
from arango_handler.arango_objs.arango_prep_document import ArangoPrepDocument
from consts import EntryConsts, KeywordConsts, ArangoConsts, StatusConsts
from entries.entries_database import Entry, session
from utils import check_arango_connectivity

app = Flask(__name__)
cors = CORS(app)
main_arango_handler = ArangoHandler()


@app.route("/")
def index():
    return ArangoConsts.ARANGO_CONNECTION_SUCCESS_MSG if check_arango_connectivity(main_arango_handler) else \
        f"Welcome to the avocado life. Connnection to arango failed = {e}"


@app.route("/get_document_names/<string:collection_name>", methods=["GET", "POST"])
@cross_origin()
def get_document_names(collection_name):
    all_documents = main_arango_handler.handle_getter(ArangoConsts.DOCUMENTS_KEYWORD, collection_name)
    return {KeywordConsts.RESULT_KEYWORD: [document.title if document.title else document._key for document in
                                           all_documents]}


@app.route("/get_collection_names/<string:must_include>")
def get_collection_names(must_include):
    return {KeywordConsts.RESULT_KEYWORD: list(
        main_arango_handler.handle_getter(ArangoConsts.COLLECTION_KEYWORD, must_include))}


@app.route("/save_entries_locally", methods=['GET', 'POST'])
@cross_origin()
def save_entries_locally():
    entry_data = json.loads(request.data)

    new_entry = Entry(title=entry_data.get(EntryConsts.ENTRY_TITLE_KEY),
                      affectingCollection=entry_data.get(EntryConsts.AFFECTING_COLLECTION_KEY),
                      impactRating=entry_data.get(EntryConsts.IMPACT_RATING_KEY),
                      definingTraits=str().join(entry_data.get(EntryConsts.DEFINING_TRAITS_KEY)),
                      insertionTime=datetime.today(),
                      sentToDestination=EntryConsts.NOT_SENT_DESTINATION_STATUS)
    session.add(new_entry)
    session.commit()
    return StatusConsts.ADDED_NEW_ENTRY


@app.route("/send_entries", methods=['GET', 'POST'])
@cross_origin()
def send_entries():
    if check_arango_connectivity():
        newEntries = session.query(Entry).filter_by(sentToDestination=EntryConsts.NOT_SENT_DESTINATION_STATUS).all()
        for entry in list(newEntries):
            prep_document_obj = ArangoPrepDocument(entry.affectingCollection, entry.title, entry.impact_rating,
                                                   entry.insertionTime)
            main_arango_handler.handle_creation(ArangoConsts.ENTRY_CREATION_TYPE, prep_document_obj)

            entry.sentToDestination = EntryConsts.SENT_TO_DESTINATION_STATUS
            session.save()
        return StatusConsts.SENT_TO_ARANGO
    return ArangoConsts.ARANGO_CONNECTION_ERROR


if __name__ == '__main__':
    app.run(debug=True)
