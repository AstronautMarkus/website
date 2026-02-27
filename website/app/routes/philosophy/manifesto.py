from flask import render_template
from . import philosophy_bp

@philosophy_bp.route('/philosophy/manifesto')
def manifesto():
    return render_template('philosophy/manifesto.html')

@philosophy_bp.route('/es/philosophy/manifesto')
def manifesto_es():
    return render_template('philosophy/es/manifesto.html')