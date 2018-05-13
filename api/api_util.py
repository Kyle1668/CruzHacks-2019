from pymongo.errors import ConnectionFailure
from pymongo import DESCENDING


def valid_connection(mongo_client):
    try:
        # The ismaster command is cheap and does not require auth.
        mongo_client.admin.command('ismaster')
        return True
    except ConnectionFailure:
        return False


def generate_hacker_id(hackers_collection):
    records = hackers_collection.find()

    if records.count() > 0:
        highest_id = records.sort("id", DESCENDING)[0]["id"]
        print("highest_id: " + str(highest_id))
        return str(int(highest_id) + 1)
    else:
        return "1"
