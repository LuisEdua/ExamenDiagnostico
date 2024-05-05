from abc import ABC, abstractmethod

from src.Gestion.Domain.Entities.Student import Student


class StudentPort(ABC):
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
    def create_student(self):
        pass

    @abstractmethod
    def update_student(self):
        pass
