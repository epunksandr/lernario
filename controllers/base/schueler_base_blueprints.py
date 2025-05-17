
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.schueler_service import SchuelerService


class SchuelerBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = SchuelerService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            klasse_id=request.form.get("klasse_id")
            vorname=request.form.get("vorname")
            nachname=request.form.get("nachname")

            service.erstelle_schueler(klasse_id, vorname, nachname)
            return redirect(url_for('schueler.uebersicht'))

        @self.route(f'/loeschen/<int:schueler_id>')
        def loeschen(schueler_id):
            service.loesche_schueler(schueler_id)
            return redirect(url_for('schueler.uebersicht'))
    