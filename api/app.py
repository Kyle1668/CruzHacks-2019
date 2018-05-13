from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from hacker_profile import HackerProfile
from bson.json_util import dumps

app = Flask(__name__)

db_uri = "mongodb://kyle:codeslug@ds221990.mlab.com:21990/cruzhacks-hackers"
mongo_client = MongoClient(db_uri)


def valid_connection():
    try:
        # The ismaster command is cheap and does not require auth.
        mongo_client.admin.command('ismaster')
        return True
    except ConnectionFailure:
        print("Server not available")
        return False


@app.route("/hackers/")
def get_all_hackers():
    if valid_connection():
        request_results = []
        query = mongo_client["cruzhacks-hackers"]["hackers"].find()

        for record in list(query):
            hacker = HackerProfile(1, name=record["name"], email=record["email"], college=record["college"])
            data = hacker.get_data()
            request_results.append(data)

        return jsonify(count=len(request_results), results=request_results)
    return "bad connection"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
