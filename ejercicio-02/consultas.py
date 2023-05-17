from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from crear_base import Pais

from crear_base import engine

Session = sessionmaker(bind=engine)
session = Session()

print("Presentar todos los países del continente americano:\n")

paises = session.query(Pais).filter(Pais.con=="NA").all()
print(paises)
print("--------------------------------")

print("Presentar los países de Asía, ordenados por el atributo Dial:\n")

paises2 = session.query(Pais).filter(Pais.con=="AS").order_by(Pais.dial).all()
print(paises2)
print("--------------------------------")

print("Presentar los lenguajes de cada país:\n")

paises3 = session.query(Pais).filter(Pais.lan!=None).all()
print(paises3)
print("--------------------------------")

print("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa:\n")
paises4 = session.query(Pais).filter(Pais.con=="EU").order_by(Pais.cap).all()
print(paises4)
print("--------------------------------")

print("Presentar todos los países que tengan en su cadena de nombre de país uador o en su cadena de capital ito :\n")
paises5 = session.query(Pais).filter(and_(Pais.name.like("%uador%"), Pais.cap.like("%ito%"))).order_by(Pais.name).all()
print(paises5)
print("--------------------------------")