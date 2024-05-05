from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port
from src.Gestion.Aplication.UseCase.Students.ListByTutor import ListByTutorUseCase as UseCase


class ListByTutorController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, tutor_uuid):
        return self.use_case.run(tutor_uuid)
