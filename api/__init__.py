"""creating app"""
import os

from flask import Flask 
from instance.config import app_config
from .v1.views import view_parties, start_views
from .v1.views.start_views import bp

"""create app with specified config"""
def create_app(config_name):
 
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	# register blueprint
	app.register_blueprint(bp)

	return app

