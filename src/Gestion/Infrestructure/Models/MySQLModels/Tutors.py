from src.DataBase.MySQL.connection import Base
from sqlalchemy import Column, String, Integer


class Tutors(Base):
    __tablename__ = 'tutors'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    hours = Column(Integer, nullable=False)
    career = Column(String(255), nullable=False)



    def to_dict(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "lastname": self.lastname,
            "hours": self.hours,
            "career": self.career
        }
