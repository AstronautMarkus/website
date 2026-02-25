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

@home_bp.route('/es')
def index_es():

    born_day = '16 de marzo de 2003'

    current_year = datetime.now().year
    born_year = datetime.strptime('2003-03-16', '%Y-%m-%d').year

    current_age = current_year - born_year

    quotes = [
        "SI EL CÓDIGOS FUNCIONA, ¡NO LO TOQUES! - 2003, CREADO POR UN HUMANO, PARA HUMANOS",
        "ESPERA, SI EL AMOR ES LA RESPUESTA, ESTÁS EN CASA.",
        "NO SOY UN ROBOT, SOY UN SER HUMANO.",
        "EN UN MUNDO DE MALAS PERSONAS, EL MAYOR ACTO DE REBELIÓN ES SER BUENO.",
        "LA VIDA ES UN VIAJE, DISFRUTA EL CAMINO.",
        "LA FELICIDAD NO ES UN DESTINO, ES UNA FORMA DE VIAJAR.",
        "LA VIDA ES DEMASIADO CORTA PARA PREOCUPARSE POR COSAS PEQUEÑAS.",
        "LA TECNOLOGÍA ES REEMPLAZABLE, LAS PERSONAS NO.",
        "¿SER FELIZ O ENCAJAR EN LA SOCIEDAD?",
        "EL DESTINO DE LAS GRANDES ALMAS ES SER CRITICADAS POR LOS MEDIOCRES.",
        "NO IMPORTA A DÓNDE VAYAS, TODOS ESTÁN CONECTADOS."
    ]

    random_quote = random.choice(quotes)

    return render_template('/es/index.html', age=current_age, born_day=born_day, quote=random_quote)