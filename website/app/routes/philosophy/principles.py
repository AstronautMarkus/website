from flask import render_template
from . import philosophy_bp

@philosophy_bp.route('/philosophy/principles')
def principles():
    return render_template('philosophy/principles.html')

@philosophy_bp.route('/es/philosophy/principles')
def principles_es():
    return render_template('philosophy/es/principles.html')