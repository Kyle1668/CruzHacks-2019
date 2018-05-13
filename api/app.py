from flask import Flask
from flask import jsonify
import api_util


app = Flask(__name__)


@app.route("/hackers/", methods=["GET"])
def get_all_hackers():
    if api_util.valid_connection():
        request_results = api_util.get_all_hackers()
        return jsonify(count=len(request_results), results=request_results)
    return "bad connection"


@app.route("/hackers/<hacker_id>", methods=["GET"])
def get_hacker(hacker_id):
    if api_util.valid_connection():
        request_result = api_util.get_hacker(hacker_id)
        return jsonify(request_result)
    return "bad connection"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=300, debug=True)
