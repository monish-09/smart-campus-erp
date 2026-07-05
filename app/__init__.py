from flask import Flask, render_template
from config import Config
from app.extensions import db, migrate, login_manager
from app.models import User
from app.auth import auth

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(auth)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app