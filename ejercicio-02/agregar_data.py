from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests

from crear_base import Pais

import json

engine = create_engine('sqlite:///paises.db')

Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

documentos = archivo.json()

for d in documentos:
    print(d)
    print(len(d.keys()))
    p = Pais(name=d['CLDR display name'], cap=d['Capital'], con=d['Continent'], \
            dial=d['Dial'], geo=d['Geoname ID'], itu=d['ITU'], lan=d['Languages'], ind=d['is_independent'])
    session.add(p)

session.commit()