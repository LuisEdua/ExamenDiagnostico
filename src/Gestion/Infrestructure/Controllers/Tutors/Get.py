from src.Gestion.Domain.Port.TutorsPort import TutorsPort as Port
from src.Gestion.Aplication.UseCase.Tutors.Get import GetUseCase as UseCase


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self):
        return self.use_case.run()
