from flask import request, redirect, url_for, flash, Blueprint, render_template
from services import class_service

noten_bp = Blueprint('noten', __name__, url_prefix="/noten")

@noten_bp.route('/')
def noten():
    return render_template('noten.html', active_page="noten")