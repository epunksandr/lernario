
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.faecher_service import FaecherService


class FaecherBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = FaecherService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            fach=request.form.get("fach")

            service.erstelle_fach(fach)
            return redirect(url_for('faecher.uebersicht'))

        @self.route(f'/loeschen/<int:fach_id>')
        def loeschen(fach_id):
            service.loesche_fach(fach_id)
            return redirect(url_for('faecher.uebersicht'))
    