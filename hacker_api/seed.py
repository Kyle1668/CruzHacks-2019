import names
import random
import pymongo
from api import mongo_client, hackers_collection, new_hacker


print("Deleting Previous Records")

hackers_collection.remove()

print("Seeding Database")

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


print("Database Seeded")

