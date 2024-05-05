import uuid


class Students:
    def __init__(self, name, lastname, grade, group, status):
        self.uuid = uuid.uuid4()
        self.name = name
        self.lastname = lastname
        self.grade = grade
        self.group = group
        self.status = status
        self.tutor_uuid = None
