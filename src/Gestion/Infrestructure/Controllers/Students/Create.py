from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port
from src.Gestion.Aplication.UseCase.Students.Create import CreateUseCase as UseCase


class CreateController:
    def __init__(self, repository: Port):
        self.use_case=UseCase(repository)

    def run(self, request):
        self.use_case.run(request.get_json())
