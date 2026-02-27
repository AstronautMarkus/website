from flask import render_template
from . import philosophy_bp

@philosophy_bp.route('/philosophy')
def philosophy_index():
    return render_template('philosophy/index.html')

@philosophy_bp.route('/es/philosophy')
def philosophy_index_es():
    return render_template('philosophy/es/index.html')