from src.Gestion.Domain.Entities.Tutors import Tutors
from abc import ABC, abstractmethod


class TutorsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_tutors(self):
        pass

    @abstractmethod
    def create_tutor(self, tutors: Tutors):
        pass
