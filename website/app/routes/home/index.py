from flask import render_template
from . import home_bp
from app.models.models import Note

@home_bp.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)