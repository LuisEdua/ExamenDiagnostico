from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port


class UpdateUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        return self.repository.update_student(**data)
