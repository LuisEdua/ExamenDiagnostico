from src.Gestion.Infrestructure.Models.MySQLModels.Subjects import Subjects as Model
from src.Gestion.Domain.Entities.Subjects import Subjects
from src.Gestion.Domain.Port.SubjectsPort import SubjectsPort
from src.DataBase.MySQL.connection import Base, engine, session_local


class SubjectsRepository(SubjectsPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_subjects(self):
        return [s.to_dict() for s in self.db.query(Model).all()]

    def create_subject(self, subject: Subjects):
        new = Model(**subject.__dict__)
        self.db.add(new)
        self.db.commit()
        return new.to_dict()
