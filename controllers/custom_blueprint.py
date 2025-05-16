from flask import Blueprint, redirect, url_for

class CustomBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route("/custom")
        def info():
            return "CUSTOM"

        @self.route(f'/loeschen/<int:id>')
        def loeschen(id):
            exec(f"{name}_service.loesche_{name}({id})")
            return redirect(url_for('schueler.uebersicht'))