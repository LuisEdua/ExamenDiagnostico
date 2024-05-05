from src.Gestion.Domain.Port.SubjectsPort import SubjectsPort as Port
from src.Gestion.Aplication.UseCase.Subjects.Create import CreateUseCase as UseCase


class CreateController:
    def __init__(self, repository: Port):
        self.use_case = UseCase(repository)

    def run(self, request):
        return self.use_case.run(request.get_json())
