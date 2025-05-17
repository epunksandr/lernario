
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.lehrer_service import LehrerService


class LehrerBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = LehrerService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            vorname=request.form.get("vorname")
            nachname=request.form.get("nachname")
            email=request.form.get("email")
            passwort_hash=request.form.get("passwort_hash")

            service.erstelle_lehrer(vorname, nachname, email, passwort_hash)
            return redirect(url_for('lehrer.uebersicht'))
            
        @self.route(f'/aktualisieren', methods=["GET, POST"])
        def aktualisieren():
            vorname=request.form.get("vorname")
            nachname=request.form.get("nachname")
            email=request.form.get("email")
            passwort_hash=request.form.get("passwort_hash")

            service.aktualisiere_lehrer(vorname, nachname, email, passwort_hash)
            return redirect(url_for('lehrer.uebersicht'))

        @self.route(f'/loeschen/<int:lehrer_id>')
        def loeschen(lehrer_id):
            service.loesche_lehrer(lehrer_id)
            return redirect(url_for('lehrer.uebersicht'))
    