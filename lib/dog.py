from models import Dog
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def create_table(base, engine):
    base.metadata.create_all(engine)
    engine = create_engine('sqlite:///dogs.db:')

def save(session, dog):
    session.add(dog)
    session.commit()

if __name__ == "__main__":
    engine = create_engine('sqlite:///dogs.db:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session_instance = Session()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()
def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()