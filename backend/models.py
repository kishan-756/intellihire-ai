from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InterviewResult(Base):

    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String)

    aptitude_score = Column(Integer)

    dsa_score = Column(Integer)

    technical_score = Column(Integer)