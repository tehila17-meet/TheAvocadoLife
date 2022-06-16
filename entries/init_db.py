from entries_database import *

engine = create_engine('sqlite:///entriesDatabase.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

testEntry = Entry(title="This is a test",
                  affectedCollection="Affecting-Events", impactRating=7, definingTraits="Independence",
                  insertionTime="2022-03-31 17:25:13.494841", sentToDestination=0)

session.add(testEntry)

session.commit()
