from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # Instantiate the app
    app = Flask(__name__)

    # Set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Shell context for Flask CLI
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
