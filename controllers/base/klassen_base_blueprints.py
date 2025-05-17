
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.klassen_service import KlassenService


class KlassenBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = KlassenService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            klassenname=request.form.get("klassenname")
            lehrer_id=session['current_teacher_id']

            service.erstelle_klasse(klassenname, lehrer_id)
            return redirect(url_for('klassen.uebersicht'))

        @self.route(f'/loeschen/<int:klasse_id>')
        def loeschen(klasse_id):
            service.loesche_klasse(klasse_id)
            return redirect(url_for('klassen.uebersicht'))
    