from flask import Flask, request

from util.hacker_util import generate_hacker_id, get_timestamp
from models.hacker_profile import HackerProfile
from pymongo import MongoClient

mlab_uri = "mongodb://kyle:codeslug@ds221990.mlab.com:21990/cruzhacks-hackers"
mongo_client = MongoClient(mlab_uri)
hackers_collection = mongo_client["cruzhacks-hackers"]["hackers"]


def new_hacker(data):
    """[Creates a new hacker model and adds it to the DB.]

    Arguments:
        data {[dict]} -- [The passed in json object from the POST request.]

    Returns:
        [dict] -- [The information for the newly created hacker.]
    """

    new_id = generate_hacker_id(hackers_collection)

    new_hacker = HackerProfile(new_id, None, None, None, None, None)

    if "name" in data:
        new_hacker.name = data["name"]
    if "email" in data:
        new_hacker.email = data["email"]
    if "college" in data:
        new_hacker.college = data["college"]
    if "major" in data:
        new_hacker.major = data["major"]
    if "dietary_preference" in data:
        new_hacker.dietary_preference = data["dietary_preference"]

    hackers_collection.insert(new_hacker.get_data())
    return new_hacker.get_data()


def get_all_hackers():
    """[Returns all the hackers in the database.]

    Returns:
        [list[dict]] -- [The list containing the information for each hacker.]
    """

    query = hackers_collection.find()
    request_results = []

    for record in list(query):
        hacker = HackerProfile(
            hacker_id=record["id"],
            name=record["name"],
            email=record["email"],
            college=record["college"],
            major=record["major"],
            dietary_preference=record["dietary_preference"])

        data = hacker.get_data()
        request_results.append(data)

    return request_results


def get_hacker(hacker_id):
    """[Returns a specific hacker by id.]

    Arguments:
        hacker_id {[int]} -- [The id of the target hacker.]

    Returns:
        [dict] -- [The info for the desired hacker if found. Empty if not.]
    """

    query = hackers_collection.find_one({"id": hacker_id})

    if query is not None:
        hacker = HackerProfile(
            hacker_id=query["id"],
            name=query["name"],
            email=query["email"],
            college=query["college"],
            major=query["major"],
            dietary_preference=query["dietary_preference"])

        return hacker.get_data()

    return None


def update_hacker(target_id, updates):
    """[Updates the information for a specific hacker.]

    Arguments:
        target_id {[int]} -- [The id of the target hacker.]
        updates {[dict]} -- [Contains the target entries and new values.]

    Returns:
        [dict] -- [The info for updated desired hacker if found. Empty if not.]
    """

    hacker_exists = hackers_collection.find({"id": target_id}).count() > 0

    if hacker_exists:
        hackers_collection.update_one({"id": target_id}, {"$set": updates})
        new_timestamp = {"last_updated_at": get_timestamp()}
        hackers_collection.update_one({"id": target_id}, {"$set": new_timestamp})
        return "updated!"
    else:
        "Hacker not found"


def delete_hacker(target_id):
    """[Deletes a target hacker fom the DB.]

    Arguments:
        target_id {[int]} -- [The id of the target hacker.]

    Returns:
        [str] -- [String telling whether the deletion was successful.]
    """

    status = "500"

    hacker_exists = bool(hackers_collection.find({"id": { "$in": target_id}}))

    if hacker_exists:
        hackers_collection.delete_one({"id": target_id})
        status = "200"

    return status

