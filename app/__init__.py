from flask import Flask
from config import config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app(config_name):
    """Application factory, see docs."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
