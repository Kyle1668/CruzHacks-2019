import sys
import names
import random
import pymongo
from api import mongo_client, hackers_collection, new_hacker
from api_util import valid_connection


majors = [
    "Computer Science",
    "Economics",
    "History",
    "Graphic Design",
    "Design",
    "Biology",
    "Engineering",
    "Chemistry",
    "Computer Engineering",
    "Data Science",
    "Poetry",
    "Marine Biology",
    "Fashion",
    "Finance",
    "Electrical Engineering"]


def seed_db():
    """
        Seeds the mongo database with 25 randomly generated hackers.
        This is run when the docker container is built.
    """

    for count in range(25):
        name = names.get_full_name()
        email = name.replace(" ", "").lower() + "@ucsc.edu"
        major = random.choice(majors)

        hacker = {
            "college": "UCSC",
            "name": name,
            "email": email,
            "major": major
        }

        print(hacker)

        new_hacker(hacker)


if valid_connection(mongo_client):
    print("Deleting Previous Records")
    hackers_collection.remove()
    print("Seeding Database")
    seed_db()
    print("Database Seeded")
else:
    error_message = """    Invalid Database Connection. This is likelly caused by internet connection blocking
    acsess to MLab. Try running on a VPN or another internet connection."""
    print("\033[91m" + error_message + "\033[0m")
    sys.exit()
