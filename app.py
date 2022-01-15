from flask import Flask, request, json
from pyArango import document
from arango_handler.arango_handler import ArangoHandler
from flask_cors import CORS, cross_origin
from consts import ApiConsts, KeywordConsts, ArangoConsts, SystemConsts
from utils import get_document_with_date, read_file_data, move_entry_to_backup
import os


app = Flask(__name__)
cors = CORS(app)

TEST_COLLECTION = "defining_traits"
master_arango_handler = ArangoHandler()

def check_arango_connectivity():
    return False if master_arango_handler.arango_connection == ArangoConsts.ARANGO_CONNECTION_ERROR else True


@app.route("/")
def index():
    return f"Welcome to the avocado life. Connection To Arango Is Established" if check_arango_connectivity else f"Welcome to the avocado life. Connnection to arango failed = {e}"


@app.route("/get_document_names/<string:collection_name>", methods=["GET", "POST"])
@cross_origin()
def get_document_names(collection_name):
    arango_collection = master_arango_handler.get_collection_obj(collection_name)
    all_documents = arango_collection.fetchAll()
    return {KeywordConsts.RESULT_KEYWORD: [document.title if document.title else document._key for document in all_documents]}

@app.route("/get_collection_names/<string:must_include>")
def get_collection_names(must_include):
    return {KeywordConsts.RESULT_KEYWORD : list(master_arango_handler.get_collection_names(must_include))}


@app.route("/save_entries", methods = ['GET', 'POST'])
@cross_origin()
def save_entries():
    entry_data = json.loads(request.data)
    entry_title = entry_data.get(ApiConsts.ENTRY_TITLE_KEY)
    base_document_data = get_document_with_date(entry_data)

    with open(os.path.join(SystemConsts.BASE_ENTRIES_DIR, '') + str(entry_title) + ".txt", "w") as entry_data_file:
        print(entry_data_file)
        entry_data_file.write(json.dumps(base_document_data))
        
    return "Saved Entry"    

@app.route("/add_entries", methods = ['GET', 'POST'])
@cross_origin()
def add_entries():
    if check_arango_connectivity():

        for root, _, files in os.walk(SystemConsts.BASE_ENTRIES_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                entry_data = read_file_data(full_path)
                collection_name, defining_traits = entry_data.get(ApiConsts.AFFECTING_COLLECTION_KEY), entry_data.get(ApiConsts.AFFECTED_COLLECTION_KEY)
                master_arango_handler.add_new_entry(collection_name, entry_data, defining_traits)
                move_entry_to_backup(full_path, file)
                
        return "Added Entry"    
    return ArangoConsts.ARANGO_CONNECTION_ERROR


if __name__ == '__main__':
    app.run(debug = True)
