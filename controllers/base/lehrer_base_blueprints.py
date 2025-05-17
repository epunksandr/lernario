
from flask import Blueprint, redirect, url_for, request, session
from services.lehrer_service import LehrerService


class LehrerBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = LehrerService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            service.erstelle_lehrer(
                request.form.get("vorname"),
                request.form.get("nachname"),
                request.form.get("email"),
                request.form.get("passwort_hash")    
            )
            return redirect(url_for('lehrer.uebersicht'))

        @self.route(f'/loeschen/<int:lehrer_id>')
        def loeschen(lehrer_id):
            service.loesche_lehrer(lehrer_id)
            return redirect(url_for('lehrer.uebersicht'))
    