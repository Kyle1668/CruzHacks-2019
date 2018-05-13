import datetime
import time

from pymongo import DESCENDING
from pymongo.errors import ConnectionFailure


def valid_connection(mongo_client):
    try:
        # The ismaster command is cheap and does not require auth.
        mongo_client.admin.command('ismaster')
        return True
    except ConnectionFailure:
        return False


def get_timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def generate_hacker_id(hackers_collection):
    records = hackers_collection.find()

    if records.count() > 0:
        highest_id = int(records.sort("id", DESCENDING)[0]["id"])
        return str(highest_id + 1)
    else:
        return "1"
