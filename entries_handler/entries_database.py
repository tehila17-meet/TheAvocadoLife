from typing import List
from sqlalchemy import Column, Integer,String, DateTime, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func


Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key = True)
    title = Column(String)
    affectingCollection = Column(String)
    impactRating = Column(Integer)
    definingTraits = Column(String)
    insertionTime = Column(DateTime)
    sentToDestination = Column(Integer) # 1 is for sent, 0 for not yet sent

engine = create_engine('sqlite:///entriesDatabase.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()