from src.Gestion.Infrestructure.Models.MySQLModels.Tutors import Tutors as Model
from src.Gestion.Domain.Port.TutorsPort import TutorsPort
from src.Gestion.Domain.Entities.Tutors import Tutors
from src.DataBase.MySQL.connection import Base, engine, session_local


class TutorsRepository(TutorsPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_tutors(self):
        return [t.to_dict() for t in self.db.query(Model).all()]

    def create_tutor(self, tutors: Tutors):
        new = Model(**tutors.__dict__)
        self.db.add(new)
        self.db.commit()
        return new.to_dict()