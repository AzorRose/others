from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Connection():
    
    def __init__(self):
        self.engine = engine_init()
        Base.metadata.create_all(self.engine)
        
    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
        
    def clear(self):
        with self.get_session() as session:
            session.query(Students).delete()
            session.commit()
        
    def add(self, names):        
        with self.get_session() as session:
            if type(names) is list:
                session.add_all(names)
            else:
                session.add(names)
            session.commit()

    def get_all(self):
        with self.get_session() as session:
            return session.query(Students).order_by(Students.id).all()
    
    def get_last(self):
        with self.get_session() as session:
            return session.query(Students).order_by(Students.id.desc()).first()


def engine_init():
    engine = create_engine(
    "postgresql+psycopg2://postgres:12345@localhost/mobile",
                       pool_size=6, max_overflow=10)

    return engine


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    

    
