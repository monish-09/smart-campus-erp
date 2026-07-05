from flask import Flask

def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    @app.route("/")
    def home():
        return "<h1>Smart Campus ERP</h1>"

    return app