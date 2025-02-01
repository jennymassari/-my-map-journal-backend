from flask import Flask
from flask_cors import CORS
from .db import db, migrate
from .models.country import Country
from .models.experience import Experience
from .routes.country_routes import bp as country_bp
from .routes.experience_routes import bp as experience_bp
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings for testing
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(country_bp, url_prefix='/country')
    app.register_blueprint(experience_bp, url_prefix='/country')

    CORS(app)
    return app