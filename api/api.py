from flask import Flask, request

from api_util import generate_hacker_id
from hacker_profile import HackerProfile
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://kyle:codeslug@ds221990.mlab.com:21990/cruzhacks-hackers")
hackers_collection = mongo_client["cruzhacks-hackers"]["hackers"]


def get_all_hackers():
    query = hackers_collection.find()
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


def get_hacker(hacker_id):
    query = hackers_collection.find_one({"id": hacker_id})

    if query is not None:
        hacker = HackerProfile(
            hacker_id=query["id"],
            name=query["name"],
            email=query["email"],
            college=query["college"])

        return {"results": hacker.get_data()}

    return {"results": None}


def new_hacker(data):
    new_id = generate_hacker_id(hackers_collection)
    new_hacker = HackerProfile(
                hacker_id=new_id,
                name=data["name"],
                email=data["email"],
                college=data["college"])

    hackers_collection.insert(new_hacker.get_data())

    return new_hacker.get_data()
