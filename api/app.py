from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from hacker_profile import HackerProfile

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
        query = mongo_client["cruzhacks-hackers"]["hackers"].find()
        request_results = []

        for record in list(query):

            hacker = HackerProfile(
                hacker_id=record["id"],
                name=record["name"],
                email=record["email"],
                college=record["college"])

            data = hacker.get_data()
            request_results.append(data)

        return jsonify(count=len(request_results), results=request_results)
    return "bad connection"


@app.route("/hackers/<hacker_id>")
def get_hacker(hacker_id):
    if valid_connection():
        query = mongo_client["cruzhacks-hackers"]["hackers"].find_one({"id": hacker_id})

        if query is not None:
            hacker = HackerProfile(
                hacker_id=query["id"],
                name=query["name"],
                email=query["email"],
                college=query["college"])

            return jsonify(count=1, results=hacker.get_data())

        return jsonify(count=0, results={})
    return "bad connection"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
