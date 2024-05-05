from abc import ABC, abstractmethod
from src.Gestion.Domain.Entities.Students import Students


class StudentsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_student(self):
        pass

    @abstractmethod
    def get_by_tutor(self, tutor_uuid):
        pass

    @abstractmethod
    def create_student(self, students: Students):
        pass

    @abstractmethod
    def update_student(self, student_uuid, tutor_uuid):
        pass
