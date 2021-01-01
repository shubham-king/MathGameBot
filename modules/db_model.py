from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    difficulty = Column(Integer)
    sum = Column(Boolean)
    sub = Column(Boolean)
    mul = Column(Boolean)
    div = Column(Boolean)

    def __init__(self, id):
        self.id = id
        self.score = 0
        self.difficulty = 0
        self.sum = True
        self.sub = True
        self.mul = False
        self.div = False
