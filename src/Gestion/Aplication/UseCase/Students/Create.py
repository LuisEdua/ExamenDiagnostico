from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port, Students as Entity


class CreateUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        return self.repository.create_student(Entity(**data))
