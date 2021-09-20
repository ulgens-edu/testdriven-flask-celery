import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from project.config import config

# Instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    # Instantiate the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Shell context for Flask CLI
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
