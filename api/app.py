from flask import Flask
from flask import jsonify
from api_util import get_every_hacker
from api_util import get_single_hacker
from api_util import valid_connection


app = Flask(__name__)


@app.route("/hackers/")
def get_all_hackers():
    if valid_connection():
        request_results = get_every_hacker()
        return jsonify(count=len(request_results), results=request_results)
    return "bad connection"


@app.route("/hackers/<hacker_id>")
def get_hacker(hacker_id):
    if valid_connection():
        request_result = get_single_hacker(hacker_id)
        return jsonify(request_result)
    return "bad connection"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
