import glob
import importlib.util
import os
import inspect

def generate_code(name1g, name1k, name2k, attributes):
    name2g = name2k.capitalize()
    methoden_attribute = ""
    konstruktor_attribute = ""
    setzen_der_attribute = ""

    for attribut in attributes:
        line = attribut + ", "
        methoden_attribute += line
        konstruktor_attribute += ( attribut + "=" + attribut + ", " )
        setzen_der_attribute += ( "        " + attribut + "=" + attribut + "\n" )

    methoden_attribute = methoden_attribute[:-2]
    konstruktor_attribute = konstruktor_attribute[:-2]

    return f"""
from db.db import SessionLocal
from models.{name2k} import {name1g}
from abc import ABC, abstractmethod

class {name2g}BaseService(ABC):

    @abstractmethod
    def gib_alle_{name2k}_von_lehrer(self, lehrer_id):
        pass

    def erstelle_{name1k}(self, {methoden_attribute}):
        session = SessionLocal()
        new_obj = {name1g}({konstruktor_attribute})
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_{name1k}(self, {name1k}_id):
        session = SessionLocal()
        obj = session.query({name1g}).filter_by({name1k}_id={name1k}_id).first()
        session.close()
        return obj
    
    def aktualisiere_{name1k}(self, {name1k}_id, {methoden_attribute}):
        session = SessionLocal()
        obj = self.gib_{name1k}({name1k}_id)
{setzen_der_attribute}
        session.commit()
        session.close()
    
    def loesche_{name1k}(self, {name1k}_id):
        session = SessionLocal()
        obj = self.gib_{name1k}({name1k}_id)
        session.delete(obj)
        session.commit()
        session.close()
    """

os.chdir("..")
model_files = glob.glob('models/*.py')

for file in model_files:
    module_name = os.path.splitext(os.path.basename(file))[0]
    spec = importlib.util.spec_from_file_location(module_name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and hasattr(obj, '__table__'):

            name1g = name
            name2k = obj.__tablename__
            name1k = name.lower()

            attributes = []
            for column in obj.__table__.columns:
                if column.primary_key:
                    pk = column.name
                else:
                    attributes.append(column.name)

            code = generate_code(name1g, name1k, name2k, attributes)
            with open(f'services/base/{name2k}_base_service.py', 'w') as file:
                file.write(code)
