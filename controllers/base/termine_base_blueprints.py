
from flask import Blueprint, redirect, url_for, request, session
from services.termine_service import TermineService


class TermineBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = TermineService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            service.erstelle_termin(
                request.form.get("termin_name"),
                request.form.get("datum"),
                request.form.get("klasse_id"),
                request.form.get("beschreibung")    
            )
            return redirect(url_for('termine.uebersicht'))

        @self.route(f'/loeschen/<int:termin_id>')
        def loeschen(termin_id):
            service.loesche_termin(termin_id)
            return redirect(url_for('termine.uebersicht'))
    