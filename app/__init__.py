from flask import Flask
from config import Config
from app.extensions import db, migrate
from app.models import User

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return "<h1>Smart Campus ERP</h1>"

    return app