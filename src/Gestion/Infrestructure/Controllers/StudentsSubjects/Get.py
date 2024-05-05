from src.Gestion.Domain.Port.StudentsSubjectsPort import StudentsSubjectsPort as Port
from src.Gestion.Aplication.UseCase.StudentsSubjects.Get import GetUseCase as UseCase


class GetController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, student_uuid):
        return self.use_case.run(student_uuid)
