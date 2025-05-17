
from flask import Blueprint, redirect, url_for, request, session
from datetime import datetime
from services.unterrichte_service import UnterrichteService


class UnterrichteBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = UnterrichteService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            lehrer_id=session['current_teacher_id']
            fach_id=request.form.get("fach_id")
            klasse_id=request.form.get("klasse_id")

            service.erstelle_unterricht(lehrer_id, fach_id, klasse_id)
            return redirect(url_for('unterrichte.uebersicht'))

        @self.route(f'/loeschen/<int:unterricht_id>')
        def loeschen(unterricht_id):
            service.loesche_unterricht(unterricht_id)
            return redirect(url_for('unterrichte.uebersicht'))
    