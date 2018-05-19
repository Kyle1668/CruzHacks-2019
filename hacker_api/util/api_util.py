from pymongo.errors import ConnectionFailure


def valid_connection(mongo_client):
    """[Tests wether there is a connection to the DB.]

    The ismaster command is cheap and does not require auth.

    Arguments:
        mongo_client {[Object]} -- [The client connection to the DB.]

    Returns:
        [bool] -- [Whether the connection was successful.]
    """

    try:
        mongo_client.admin.command('ismaster')
        return True
    except ConnectionFailure:
        return False
