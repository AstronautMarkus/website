
from flask import render_template
from . import home_bp
from datetime import datetime

@home_bp.route('/')
def index():

    born_day = '2003-03-16'

    current_year = datetime.now().year
    born_year = datetime.strptime(born_day, '%Y-%m-%d').year

    current_age = current_year - born_year

    return render_template('index.html', age=current_age, born_day=born_day)