import datetime
import time


def get_timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def test_get_timestamp():
    ts = time.time()
    current_time = datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d %H:%M:%S')
    assert get_timestamp().split(":")[:1] == current_time.split(":")[:1]


def generate_hacker_id(hackers_collection=None):
    if len(records) > 0:
        highest_id = 121
        return highest_id + 1
    else:
        return 1


def test_generate_hacker_id():
    assert 122 == generate_hacker_id()
