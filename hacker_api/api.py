from flask import Flask, request

from api_util import generate_hacker_id, get_timestamp
from hacker_profile import HackerProfile
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
    new_hacker = HackerProfile(
        hacker_id=new_id,
        name=data["name"],
        email=data["email"],
        college=data["college"],
        major=data["major"])

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
            major=record["major"])

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
            hacker_id=record["id"],
            name=record["name"],
            email=record["email"],
            college=record["college"],
            major=record["major"])

        return {"results": hacker.get_data()}

    return {"results": None}


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
        hackers_collection.update_one(
            {"id": target_id}, {"$set": {"last_updated_at": get_timestamp()}})
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

    hacker_exists = hackers_collection.find({"id": target_id}).count() > 0

    if hacker_exists:
        hackers_collection.remove({"id": target_id})
        return "deleted!"
    else:
        "Hacker not found"
