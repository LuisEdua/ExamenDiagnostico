from uuid import uuid4


class Subjects:
    def __init__(self, name):
        self.uuid = uuid4()
        self.name = name
