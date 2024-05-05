from src.Gestion.Domain.Port.SubjectsPort import SubjectsPort as Port, Subjects as Entity


class CreateUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        return self.repository.create_subject(Entity(**data))
