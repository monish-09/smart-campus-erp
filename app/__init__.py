from flask import Flask,render_template
from config import Config
from app.extensions import db, migrate
from app.models import User
from app.auth import auth


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app