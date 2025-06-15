from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String)
    email = Column(String)
    phone = Column(Integer)

def get_engine(db_path: str = "mydata.db"):
    return create_engine(f"sqlite:///{db_path}", echo=False)

def get_session(engine):
    return Session(engine)
