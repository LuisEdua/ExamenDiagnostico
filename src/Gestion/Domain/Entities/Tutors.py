from uuid import uuid4


class Tutors:
    def __init__(self, name, lastname, hours, career):
        self.uuid = uuid4()
        self.name = name
        self.lastname = lastname
        self.hours = hours
        self.career = career
