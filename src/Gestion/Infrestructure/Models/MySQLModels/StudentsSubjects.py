from sqlalchemy.orm import relationship, backref
from src.DataBase.MySQL.connection import Base
from sqlalchemy import Column, String, ForeignKey
from src.Gestion.Infrestructure.Models.MySQLModels.Students import Students
from src.Gestion.Infrestructure.Models.MySQLModels.Subjects import Subjects


class StudentsSubjects(Base):
    __tablename__ = "students_subjects"
    uuid = Column(String(36), primary_key=True)
    student_uuid = Column(String(36), ForeignKey("students.uuid"), nullable=False)
    student = relationship(Students, backref=backref("students_subjects"), cascade="all, delete")
    subject_uuid = Column(String(36), ForeignKey("subjects.uuid"), nullable=False)
    subject = relationship(Subjects, backref=backref("students_subjects"), cascade="all, delete")


    def to_dict(self):
        return {
            "uuid": self.uuid,
            "subject": self.subject.to_dict()
        }
