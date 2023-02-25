from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    affectingCollection = Column(String)
    impactRating = Column(Integer)
    definingTraits = Column(String)
    insertionTime = Column(DateTime)
    sentToDestination = Column(Integer)  # 1 is for sent, 0 for not yet sent
#sqlite:///entriesDatabase.db
engine = create_engine("sqlite:///C:\\Users\\Tehila\\Desktop\\Avocado\\Backend\\entriesDatabase.db", connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
