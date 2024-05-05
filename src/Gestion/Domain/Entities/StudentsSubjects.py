from uuid import uuid4


class StudentsSubjects:
    def __init__(self, student_uuid, subject_uuid):
        self.uuid = uuid4()
        self.student_uuid = student_uuid
        self.subject_uuid = subject_uuid
