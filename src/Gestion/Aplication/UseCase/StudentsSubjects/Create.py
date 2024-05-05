from src.Gestion.Domain.Port.StudentsSubjectsPort import StudentsSubjectsPort as Port, StudentsSubjects as Entity


class CreateUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        return self.repository.create_student_subject(Entity(**data))
