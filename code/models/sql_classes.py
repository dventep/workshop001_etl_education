""" This module is to declarative the SQL classes for the database """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Raw_Applicant(Base):
    __tablename__ = "raw_applicant"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True, default=None)
    last_name = Column(String(50), nullable=True, default=None)
    email = Column(String(60), nullable=True, default=None)
    applicant_date = Column(String(20), nullable=True, default=None)
    country = Column(String(40), nullable=True, default=None)
    experience_year = Column(Integer(), nullable=True, default=None)
