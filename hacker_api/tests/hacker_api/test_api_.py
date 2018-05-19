def get_hackers():
    """[Returns all the hackers in the database.]

    Returns:
        [flask.Response] -- [The JSON list containing the information for each hacker.]
    """

    if valid_connection(application.mongo_client):
        request_results = application.get_all_hackers()
        return jsonify(code="200", message="Hackers retrieved successfully.", count=len(request_results), results=request_results)

    return jsonify(code="500", message="Unable to connect to database.")