from src.Gestion.Domain.Entities.Subjects import Subjects
from abc import ABC, abstractmethod


class SubjectsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_subjects(self):
        pass

    @abstractmethod
    def create_subject(self, subject: Subjects):
        pass
