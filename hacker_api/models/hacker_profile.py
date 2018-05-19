import datetime
import time

from util.hacker_util import get_timestamp


class HackerProfile:
    def __init__(self, hacker_id, name, email, college, major):
        self.id = hacker_id
        self.name = name
        self.email = email
        self.college = college
        self.major = major
        self.created_at = self.get_timestamp()
        self.last_updated_at = self.get_timestamp()

    def get_timestamp(self):
        ts = time.time()
        return datetime.datetime.fromtimestamp(ts).strftime(
            '%Y-%m-%d %H:%M:%S')

    def get_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "college": self.college,
            "major": self.major,
            "created_at": self.created_at,
            "last_updated_at": self.last_updated_at
        }
