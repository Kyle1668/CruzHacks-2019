from flask import Flask, jsonify, request

import application
from util.api_util import valid_connection

app = Flask(__name__)


@app.route("/hackers/", methods=["GET"])
def get_hackers():
    """[Returns all the hackers in the database.]

    Returns:
        [flask.Response] -- [The JSON list containing the information for each hacker.]
    """

    if valid_connection(application.mongo_client):
        request_results = application.get_all_hackers()
        return jsonify(code="200", message="Hackers retrieved successfully.", count=len(
            request_results), results=request_results)

    return jsonify(code="500", message="Unable to connect to database.")


@app.route("/hackers/<hacker_id>", methods=["GET"])
def get_hacker(hacker_id):
    """[Returns a specific hacker by id.]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [flask.Response] -- [The JSON list containing the information for each hacker.]
    """

    try:
        hacker_id = int(hacker_id)
    except ValueError:
        return jsonify(code="400", message="Hacker ID must be an integer.")

    if valid_connection(application.mongo_client):
        request_result = application.get_hacker(hacker_id)
        return jsonify(
            code="200", message="Hacker retrieved successfully.", results=request_result)

    return jsonify(code="500", message="Unable to connect to database.")


@app.route("/hackers/", methods=["POST"])
def create_new_hacker():
    """[Creates a new hacker model and adds it to the DB.]

    Returns:
        [flask.Response] -- [The information for the newly created hacker in JSON.]
    """

    try:
        hacker_id = int(hacker_id)
    except ValueError:
        return jsonify(code="400", message="Hacker ID must be an integer.")

    if valid_connection(application.mongo_client):
        new_hacker = application.new_hacker(data=request.json)
        return jsonify(
            code="200", message="Hacker created successfully.", results=new_hacker)

    return jsonify(code="500", message="Unable to connect to database.")


@app.route("/hackers/<hacker_id>", methods=["PUT"])
def update_hacker(hacker_id):
    """[Returns a specific hacker by id.]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [dict] -- [The info for the desired hacker if found. Empty if not.]
    """

    try:
        hacker_id = int(hacker_id)
    except ValueError:
        return jsonify(code="400", message="Hacker ID must be an integer.")

    if valid_connection(application.mongo_client):
        updated_hacker = application.update_hacker(
            target_id=hacker_id,
            updates=request.json
        )
        return jsonify(
            code="200", message="Hacker updated successfully.", results=updated_hacker)

    return jsonify(code="500", message="Unable to connect to database.")


@app.route("/hackers/<hacker_id>", methods=["DELETE"])
def delete_hacker(hacker_id):
    """[Removes a specified hacker from the database. ]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [flask.Response] -- [The info for updated desired hacker if found. Empty if not.]
    """

    try:
        hacker_id = int(hacker_id)
    except ValueError:
        return jsonify(code="400", message="Hacker ID must be an integer.")

    if valid_connection(application.mongo_client):
        deleted_hacker = application.delete_hacker(
            target_id=hacker_id,
        )
        return jsonify(
            code="200", message="Hacker deleted successfully.", results=deleted_hacker)

    return jsonify(code="500", message="Unable to connect to database.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=300, debug=True)
