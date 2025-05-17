import glob
import importlib.util
import os
import inspect
from sqlalchemy.orm import DeclarativeMeta


def generate_code(name1g, name1k, name2k, attributes):
    name2g = name2k.capitalize()
    erstellen_param = ""
    for attribut in attributes:
        if attribut == "lehrer_id":
            erstellen_param += f"                session['current_teacher_id'],\n"
        else:
            erstellen_param += f"                request.form.get(\"{attribut}\"),\n"
    erstellen_param = erstellen_param[:-2]
    return f"""
from flask import Blueprint, redirect, url_for, request, session
from services.{name2k}_service import {name2g}Service


class {name2g}Blueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = {name2g}Service()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            service.erstelle_{name1k}(
{erstellen_param}    
            )
            return redirect(url_for('{name2k}.uebersicht'))

        @self.route(f'/loeschen/<int:{name1k}_id>')
        def loeschen({name1k}_id):
            service.loesche_{name1k}({name1k}_id)
            return redirect(url_for('{name2k}.uebersicht'))
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

            attributes = []
            for column in obj.__table__.columns:
                if column.primary_key:
                    pk = column.name
                else:
                    attributes.append(column.name)

            code = generate_code(name1g, name1k, name2k, attributes)
            with open(f'controllers/base/{name2k}_base_blueprints.py', 'w') as file:
                file.write(code)
