from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port
from src.Gestion.Aplication.UseCase.Students.Update import UpdateUseCase as UseCase


class UpdateController:
    def __init__(self, repository: Port):
        self.use_case=UseCase(repository)

    def run(self, request):
        return self.use_case.run(request.get_json())
