from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, backref
from src.DataBase.MySQL.connection import Base
from src.Gestion.Infrestructure.Models.MySQLModels.Tutors import Tutors


class Students(Base):
    __tablename__ = 'students'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    grade = Column(Integer, nullable=False)
    group = Column(String(1), nullable=False)
    status = Column(Boolean, nullable=False)
    tutor_uuid = Column(String(36), ForeignKey('tutors.uuid'), nullable=True)
    tutor = relationship(Tutors, backref=backref('alumnos'), uselist=True, cascade='all, delete')

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'name': self.name,
            'lastname': self.lastname,
            'grade': self.grade,
            'group': self.group,
            'status': self.status
        }


