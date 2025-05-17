
from flask import Blueprint, redirect, url_for, request, session
from services.schueler_service import SchuelerService


class SchuelerBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = SchuelerService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            service.erstelle_schueler(
                request.form.get("klasse_id"),
                request.form.get("vorname"),
                request.form.get("nachname")    
            )
            return redirect(url_for('schueler.uebersicht'))

        @self.route(f'/loeschen/<int:schueler_id>')
        def loeschen(schueler_id):
            service.loesche_schueler(schueler_id)
            return redirect(url_for('schueler.uebersicht'))
    