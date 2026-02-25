from flask import render_template
from . import home_bp
from datetime import datetime
import random

@home_bp.route('/')
def index():

    born_day = '2003-03-16'

    current_year = datetime.now().year
    born_year = datetime.strptime(born_day, '%Y-%m-%d').year

    current_age = current_year - born_year

    quotes = [
        "IF THE CODE WORKS, DON'T TOUCH IT!! - 2003, CREATED BY A HUMAN, FOR HUMANS",
        "HOLD ON, IF LOVE IS THE ANSWER, YOU'RE HOME.",
        "I'M NOT A ROBOT, I'M A HUMAN BEING.",
        "IN A WORLD OF BAD PEOPLE, THE GREATEST ACT OF REBELLION IS TO BE GOOD.",
        "LIFE IS A JOURNEY, ENJOY THE RIDE.",
        "HAPPINESS IS NOT A DESTINATION, IT'S A WAY OF TRAVELING.",
        "LIFE IS TOO SHORT TO WORRY ABOUT SMALL THINGS.",
        "TECHNOLOGY IS REPLACEABLE, PEOPLE ARE NOT.",
        "BE HAPPY OR FIT INTO SOCIETY?",
        "THE DESTINY OF GREAT SOULS IS TO BE CRITICIZED BY THE MEDIOCRE.",
        "NO MATTER WHERE YOU GO, EVERYBODY'S CONNECTED."
    ]

    random_quote = random.choice(quotes)

    return render_template('index.html', age=current_age, born_day=born_day, quote=random_quote)