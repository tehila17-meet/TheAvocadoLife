from flask import Flask, request, json
from pyArango import document
from arango_handler.arango_handler import ArangoHandler
from flask_cors import CORS, cross_origin
from consts import ApiConsts, KeywordConsts
from utils import get_document_with_date
app = Flask(__name__)
cors = CORS(app)

TEST_COLLECTION = "defining_traits"
master_arango_handler = ArangoHandler()



@app.route("/")
def index():
    arango_collection = master_arango_handler.get_collection_obj(TEST_COLLECTION)
  
    # for user in all_users:
    #     new_document = arango_collection.createDocument(user)
    #     new_document.save()

    return f"{arango_collection}"

@app.route("/get_document_names/<string:collection_name>", methods=["GET", "POST"])
@cross_origin()
def get_document_names(collection_name):
    arango_collection = master_arango_handler.get_collection_obj(collection_name)
    all_documents = arango_collection.fetchAll()
    return {KeywordConsts.RESULT_KEYWORD: [document.title if document.title else document._key for document in all_documents]}

@app.route("/get_collection_names/<string:must_include>")
def get_collection_names(must_include):
    return {KeywordConsts.RESULT_KEYWORD : list(master_arango_handler.get_collection_names(must_include))}

@app.route("/add_entries", methods = ['GET', 'POST'])
@cross_origin()
def add_entries():
    entry_data = json.loads(request.data)
    collection_name, defining_traits = entry_data.get(ApiConsts.AFFECTING_COLLECTION_KEY), entry_data.get(ApiConsts.AFFECTED_COLLECTION_KEY)
    base_document_data = {key: value for key, value in entry_data.items() if key not in [ApiConsts.AFFECTING_COLLECTION_KEY, ApiConsts.AFFECTED_COLLECTION_KEY]}
    base_document_data = get_document_with_date(base_document_data)
    master_arango_handler.add_new_entry(collection_name, base_document_data, defining_traits)

    return "Added Entry"    





if __name__ == '__main__':
    app.run(debug = True)
