class HackerProfile:

    def __init__(self, hacker_id, name, email, college):
        self.id = hacker_id
        self.name = name
        self.email = email
        self.college = college

    def get_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "college": self.college
        }
