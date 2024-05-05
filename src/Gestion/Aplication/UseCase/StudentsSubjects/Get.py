from src.Gestion.Domain.Port.StudentsSubjectsPort import StudentsSubjectsPort as Port


class GetUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, student_uuid):
        return self.repository.get_subjects_by_student(student_uuid)
