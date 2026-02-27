from flask import render_template
from . import philosophy_bp

@philosophy_bp.route('/philosophy/why-not-frameworks')
def why_not_frameworks():
    return render_template('philosophy/why_not_frameworks.html')

@philosophy_bp.route('/es/philosophy/why-not-frameworks')
def why_not_frameworks_es():
    return render_template('philosophy/es/why_not_frameworks.html')