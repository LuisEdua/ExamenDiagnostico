import uuid


class Student:
    def __init__(self, name, lastname, grade, group):
        self.uuid = uuid.uuid4()
        self.name = name
        self.lastname = lastname
        self.grade = grade
        self.group = group
        self.tutor = None
