from src.Gestion.Infrestructure.Models.MySQLModels.StudentsSubjects import StudentsSubjects as Model
from src.Gestion.Domain.Entities.StudentsSubjects import StudentsSubjects
from src.Gestion.Domain.Port.StudentsSubjectsPort import StudentsSubjectsPort
from src.DataBase.MySQL.connection import Base, engine, session_local


class StudentsSubjectsRepository(StudentsSubjectsPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_subjects_by_student(self, student_uuid):
        return [p.to_dict() for p in self.db.query(Model).filter(Model.student_uuid == student_uuid).all()]

    def create_student_subject(self, student_subject: StudentsSubjects):
        new = Model(**student_subject.__dict__)
        self.db.add(new)
        self.db.commit()
        return new.to_dict()
