import os

from flask import Flask
from flask_celeryext import FlaskCeleryExt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from project.celery_utils import make_celery
from project.config import config, config

# Instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    # Instantiate the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ext_celery.init_app(app)

    # Register blueprints
    from project.users import users_blueprint

    app.register_blueprint(users_blueprint)

    # Shell context for Flask CLI
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
