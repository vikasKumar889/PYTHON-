from tokenize import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from traitlets import Integer. Integer, String, DataTime, create_engine, ForeignKey
from datetime import datetime

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    created_date = Column(DateTime, default=datetime.now)

    def __str__(self):
        return self.name

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    publication = Column(String(50))
    pages = Column(Integer)
    author_id = Column(Integer, Foreignkey('authors.id'))
    created_date = Column(DateTime, default=datetime.now)

     de        