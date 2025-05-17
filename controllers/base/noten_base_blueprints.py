
from flask import Blueprint, redirect, url_for, request, session
from services.noten_service import NotenService


class NotenBlueprint(Blueprint):

    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        
        service = NotenService()

        @self.route(f'/erstellen', methods=["POST"])
        def erstellen():
            service.erstelle_note(
                request.form.get("schueler_id"),
                request.form.get("unterricht_id"),
                request.form.get("note")    
            )
            return redirect(url_for('noten.uebersicht'))

        @self.route(f'/loeschen/<int:note_id>')
        def loeschen(note_id):
            service.loesche_note(note_id)
            return redirect(url_for('noten.uebersicht'))
    