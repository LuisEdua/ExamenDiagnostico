from src.Gestion.Domain.Port.StudentsSubjectsPort import StudentsSubjectsPort as Port
from src.Gestion.Aplication.UseCase.StudentsSubjects.Create import CreateUseCase as UseCase


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, request):
        return self.use_case.run(request.get_json())
