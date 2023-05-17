from sqlalchemy import create_engine

#engine = create_engine('sqlite:///paises.db')
engine = create_engine("postgresql+psycopg2://invitado:UTPLUTPL@localhost:5432/demo100", echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cap = Column(String)
    con = Column(String)
    dial = Column(String)
    geo = Column(Integer)
    itu = Column(String)
    lan = Column(String)
    ind = Column(String)

def _repr_(self):
        return "Pais: name=%s cap:%s con=%s dial:%s geo:%s itu:%s lan:%s ind:%s" % (
                          
                          self.name,
                          self.cap,
                          self.con,
                          self.dial,
                          self.geo,
                          self.itu,
                          self.lan,
                          self.ind)

Base.metadata.create_all(engine)