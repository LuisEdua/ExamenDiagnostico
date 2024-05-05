from src.Gestion.Domain.Entities.StudentsSubjects import StudentsSubjects
from abc import ABC, abstractmethod


class StudentsSubjectsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_subjects_by_student(self, student_uuid):
        pass

    @abstractmethod
    def create_student_subject(self, student_subject: StudentsSubjects):
        pass
