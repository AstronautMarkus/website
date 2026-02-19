from flask import Flask
from flask import render_template


def create_app():
	app = Flask(__name__)

	from app.routes.home import home_bp
	app.register_blueprint(home_bp)

	return app
