import datetime
import time

from pymongo import DESCENDING


def get_timestamp():
    """[Returns the current timestamp.]

    Returns:
        [str] -- [The formatted timestamp.]
    """

    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def generate_hacker_id(hackers_collection):
    """[Generates a new hacker id by making it one larger than the currently largest.]

    Arguments:
        hackers_collection {[dict]} -- [The DB collection containing the hackers.]

    Returns:
        [str] -- [The new hacker id]
    """

    records = hackers_collection.find()

    if records.count() > 0:
        highest_id = int(records.sort("id", DESCENDING)[0]["id"])
        return highest_id + 1
    else:
        return 1
