from src.DataBase.MySQL.connection import Base
from sqlalchemy import Column, String


class Subjects(Base):
    __tablename__ = 'subjects'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)


    def to_dict(self):
        return {
            'uuid': self.uuid,
            'name': self.name
        }
