import glob
import importlib.util
import os
import inspect
from sqlalchemy.orm import DeclarativeMeta

def generate_code(name1g, name1k, name2k, attributes, attributes_set):
    return f"""
from db.db import SessionLocal
from models.{name2k} import {name1g}

class {name1g}BaseService:
    def erstelle_{name1k}(self, {attributes}):
        session = SessionLocal()
        new_obj = {name1g}({attributes})
        session.add(new_obj)
        session.commit()
        session.close()
    
    def gib_{name1k}(self, {name1k}_id):
        session = SessionLocal()
        obj = session.query({name1g}).filter_by({name1k}_id={name1k}_id).first()
        session.close()
        return obj
    
    def aktualisiere_{name1k}(self, {name1k}_id, {attributes}):
        session = SessionLocal()
        obj = self.gib_{name1k}({name1k}_id)
{attributes_set}
        session.commit()
        session.close()
    
    def loesche_{name1k}(self, {name1k}_id):
        session = SessionLocal()
        obj = self.gib_{name1k}({name1k}_id)
        session.delete(obj)
        session.commit()
        session.close()
    """

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

            pk = ""
            attributes = ""
            attributes_set = ""
            for column in obj.__table__.columns:
                if column.primary_key:
                    pk = column.name
                else:
                    attributes += column.name + " ,"
                    attributes_set += "        obj."
                    attributes_set += column.name
                    attributes_set += "="
                    attributes_set += column.name
                    attributes_set += "\n"

            attributes = attributes[:-2]

            code = generate_code(name1g, name1k, name2k, attributes, attributes_set)
            with open(f'services/{name2k}_base_service.py', 'w') as file:
                file.write(code)
