from src.Gestion.Domain.Port.StudentsPort import StudentsPort as Port


class ListByTutorUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, tutor_uuid):
        return self.repository.get_by_tutor(tutor_uuid)
