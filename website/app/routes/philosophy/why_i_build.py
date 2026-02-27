from flask import render_template
from . import philosophy_bp

@philosophy_bp.route('/philosophy/why-i-build')
def why_i_build():
    return render_template('philosophy/why_i_build.html')

@philosophy_bp.route('/es/philosophy/why-i-build')
def why_i_build_es():
    return render_template('philosophy/es/why_i_build.html')