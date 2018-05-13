from flask import Flask
from flask import request
from pymongo import MongoClient
from hacker_profile import HackerProfile
from pymongo.errors import ConnectionFailure


db_uri = "mongodb://kyle:codeslug@ds221990.mlab.com:21990/cruzhacks-hackers"
mongo_client = MongoClient(db_uri)


def valid_connection():
    try:
        # The ismaster command is cheap and does not require auth.
        mongo_client.admin.command('ismaster')
        return True
    except ConnectionFailure:
        print("Server not available")
        return False


def get_every_hacker():
    query = mongo_client["cruzhacks-hackers"]["hackers"].find()
    request_results = []

    for record in list(query):
        hacker = HackerProfile(
            hacker_id=record["id"],
            name=record["name"],
            email=record["email"],
            college=record["college"])

        data = hacker.get_data()
        request_results.append(data)

    return request_results


def get_single_hacker(hacker_id):
    query = mongo_client["cruzhacks-hackers"]["hackers"].find_one({"id": hacker_id})

    if query is not None:
        hacker = HackerProfile(
            hacker_id=query["id"],
            name=query["name"],
            email=query["email"],
            college=query["college"])

        return {"count": 1, "results": hacker.get_data()}
    else:
        return {"count": 0, "results": None}
