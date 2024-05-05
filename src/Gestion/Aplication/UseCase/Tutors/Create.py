from src.Gestion.Domain.Port.TutorsPort import TutorsPort as Port
from src.Gestion.Domain.Entities.Tutors import Tutors as Entity


class CreateUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        return self.repository.create_tutor(Entity(**data))
