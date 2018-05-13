from flask import Flask, request

from api_util import generate_hacker_id
from hacker_profile import HackerProfile
from pymongo import MongoClient

mlab_uri = "mongodb://kyle:codeslug@ds221990.mlab.com:21990/cruzhacks-hackers"
mongo_client = MongoClient(mlab_uri)
hackers_collection = mongo_client["cruzhacks-hackers"]["hackers"]


def new_hacker(data):
    new_id = generate_hacker_id(hackers_collection)
    new_hacker = HackerProfile(
        hacker_id=new_id,
        name=data["name"],
        email=data["email"],
        college=data["college"],
        major=data["major"])

    hackers_collection.insert(new_hacker.get_data())

    return new_hacker.get_data()


def get_all_hackers():
    query = hackers_collection.find()
    request_results = []

    for record in list(query):
        hacker = HackerProfile(
            hacker_id=record["id"],
            name=record["name"],
            email=record["email"],
            college=record["college"],
            major=record["major"])

        data = hacker.get_data()
        request_results.append(data)

    return request_results


def get_hacker(hacker_id):
    query = hackers_collection.find_one({"id": hacker_id})

    if query is not None:
        hacker = HackerProfile(
            hacker_id=record["id"],
            name=record["name"],
            email=record["email"],
            college=record["college"],
            major=record["major"])

        return {"results": hacker.get_data()}

    return {"results": None}


def update_hacker(target_id, updates):
    hacker_exists = hackers_collection.find({"id": target_id}).count() > 0

    if hacker_exists:
        hackers_collection.update_one({"id": target_id}, {"$set": updates})
        # return hackers_collection.find_one({"id": target_id})
        return "updated!"
    else:
        "Hacker not found"


def delete_hacker(target_id):
    hacker_exists = hackers_collection.find({"id": target_id}).count() > 0

    if hacker_exists:
        # hackers_collection.update_one({"id": target_id}, {"$set": updates})
        # return hackers_collection.find_one({"id": target_id})
        hackers_collection.remove({"id": target_id})
        return "deleted!"
    else:
        "Hacker not found"
