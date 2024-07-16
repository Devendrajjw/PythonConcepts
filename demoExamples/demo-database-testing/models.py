# pip install pytest sqlalchemy pytest-factoryboy

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(255), nullable=False)
    joined = Column(DateTime, default=datetime.now)
    articles = relationship('Article', backref='author')

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    slug = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
