
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.abwesenheiten_service import AbwesenheitenService


class AbwesenheitenBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = AbwesenheitenService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            schueler_id=request.form.get("schueler_id")
            datum_str=request.form.get("datum")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()

            service.erstelle_abwesenheit(schueler_id, datum)
            return redirect(url_for('abwesenheiten.uebersicht'))

        @self.route(f'/loeschen/<int:abwesenheit_id>')
        def loeschen(abwesenheit_id):
            service.loesche_abwesenheit(abwesenheit_id)
            return redirect(url_for('abwesenheiten.uebersicht'))
    