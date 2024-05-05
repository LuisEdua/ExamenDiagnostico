from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port


class GetUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self):
        return self.repository.get_student()
