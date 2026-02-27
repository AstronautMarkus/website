from flask import render_template
from . import philosophy_bp

@philosophy_bp.route('/philosophy/why-static')
def why_static():
    return render_template('philosophy/why_static.html')

@philosophy_bp.route('/es/philosophy/why-static')
def why_static_es():
    return render_template('philosophy/es/why_static.html')