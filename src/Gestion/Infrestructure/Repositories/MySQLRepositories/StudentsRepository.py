from src.DataBase.MySQL.connection import Base, engine, session_local
from src.Gestion.Infrestructure.Models.MySQLModels.Students import Students as Model
from src.Gestion.Domain.Port.StudentsPort import StudentsPort
from src.Gestion.Domain.Entities.Students import Students


class StudentsRepository(StudentsPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_student(self):
        return [s.to_dict() for s in self.db.query(Model).all()]

    def get_by_tutor(self, tutor_uuid):
        return [s.to_dict() for s in self.db.query(Model).filter(Model.tutor_uuid == tutor_uuid).all()]

    def create_student(self, students: Students):
        new = Model(**students.__dict__)
        self.db.add(new)
        self.db.commit()
        return new.to_dict()

    def update_student(self, student_uuid, tutor_uuid):
        student = self.db.query(Model).filter(Model.uuid == student_uuid).first()
        student.tutor_uuid = tutor_uuid
        self.db.commit()
        return student.to_dict()
