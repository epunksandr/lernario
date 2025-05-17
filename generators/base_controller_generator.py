import glob
import importlib.util
import os
import inspect


def generate_code(name1g, name1k, name2k, attributes):
    name2g = name2k.capitalize()
    erstellen_param = ""
    set_attributes = ""
    for attribut in attributes:
        if attribut == "lehrer_id":
            set_attributes += f"            {attribut}=session['current_teacher_id']\n"
        elif "datum" in attribut.lower():
            set_attributes += f"            datum_str=request.form.get(\"{attribut}\")\n"
            set_attributes += f"            datum = datetime.strptime(datum_str, \"%Y-%m-%d\").date()\n"
        else:
            set_attributes += f"            {attribut}=request.form.get(\"{attribut}\")\n"
        erstellen_param += f"{attribut}, "
    erstellen_param = erstellen_param[:-2]
    return f"""
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.{name2k}_service import {name2g}Service


class {name2g}Blueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = {name2g}Service()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
{set_attributes}
            service.erstelle_{name1k}({erstellen_param})
            return redirect(url_for('{name2k}.uebersicht'))
            
        @self.route(f'/aktualisieren', methods=["GET, POST"])
        def aktualisieren():
{set_attributes}
            service.aktualisiere_{name1k}({erstellen_param})
            return redirect(url_for('{name2k}.uebersicht'))

        @self.route(f'/loeschen/<int:{name1k}_id>')
        def loeschen({name1k}_id):
            service.loesche_{name1k}({name1k}_id)
            return redirect(url_for('{name2k}.uebersicht'))
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
            with open(f'controllers/base/{name2k}_base_blueprints.py', 'w') as file:
                file.write(code)
