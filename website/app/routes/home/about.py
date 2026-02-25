
from flask import render_template
from . import home_bp

@home_bp.route('/about')
def about():
    return render_template('about.html')

@home_bp.route('/es/about')
def about_es():
    return render_template('es/about.html')