
from flask import render_template
from . import home_bp

@home_bp.route('/about')
def about():

    birthday = (2003, 3, 16)
    def current_age():
        from datetime import date
        today = date.today()
        age = today.year - birthday[0] - ((today.month, today.day) < (birthday[1], birthday[2]))
        return age

    return render_template('about.html', current_age=current_age)