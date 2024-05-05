from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

DATABASE_URL = 'mysql+pymysql://admin:adminadmin@database-1.ch8hmfdp4yhn.us-east-1.rds.amazonaws.com:3306/bdg'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
session_local = sessionmaker(bind=engine)
