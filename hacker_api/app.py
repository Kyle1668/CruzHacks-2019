from flask import Flask, jsonify, request

import api
from util.api_util import valid_connection

app = Flask(__name__)


@app.route("/hackers/", methods=["GET"])
def get_all_hackers():
    """[Returns all the hackers in the database.]

    Returns:
        [flask.Response] -- [The JSON list containing the information for each hacker.]
    """

    if valid_connection(api.mongo_client):
        request_results = api.get_all_hackers()
        return jsonify(count=len(request_results), results=request_results)

    return "bad connection"


@app.route("/hackers/<hacker_id>", methods=["GET"])
def get_hacker(hacker_id):
    """[Returns a specific hacker by id.]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [flask.Response] -- [The JSON list containing the information for each hacker.]
    """

    if valid_connection(api.mongo_client):
        request_result = api.get_hacker(hacker_id)
        return jsonify(request_result)

    return "bad connection"


@app.route("/hackers/", methods=["POST"])
def new_hacker():
    """[Creates a new hacker model and adds it to the DB.]

    Returns:
        [flask.Response] -- [The information for the newly created hacker in JSON.]
    """

    if valid_connection(api.mongo_client):
        new_hacker = api.new_hacker(data=request.json)
        return jsonify(result=new_hacker)

    return "bad connection"


@app.route("/hackers/<hacker_id>", methods=["PUT"])
def update_hacker(hacker_id):
    """[Returns a specific hacker by id.]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [dict] -- [The info for the desired hacker if found. Empty if not.]
    """

    if valid_connection(api.mongo_client):
        updated_hacker = api.update_hacker(
            target_id=hacker_id,
            updates=request.json
        )

        return jsonify(result=updated_hacker)

    return "bad connection"


@app.route("/hackers/<hacker_id>", methods=["DELETE"])
def delete_hacker(hacker_id):
    """[summary]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [flask.Response] -- [The info for updated desired hacker if found. Empty if not.]
    """

    if valid_connection(api.mongo_client):
        deleted_hacker = api.delete_hacker(
            target_id=hacker_id,
        )

        return jsonify(result=deleted_hacker)

    return "bad connection"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=300, debug=True)
