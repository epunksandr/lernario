
from flask import Blueprint, redirect, url_for, request, session
from services.unterrichte_service import UnterrichteService


class UnterrichteBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = UnterrichteService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            service.erstelle_unterricht(
                session['current_teacher_id'],
                request.form.get("fach_id"),
                request.form.get("klasse_id")    
            )
            return redirect(url_for('unterrichte.uebersicht'))

        @self.route(f'/loeschen/<int:unterricht_id>')
        def loeschen(unterricht_id):
            service.loesche_unterricht(unterricht_id)
            return redirect(url_for('unterrichte.uebersicht'))
    