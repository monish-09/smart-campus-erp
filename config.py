import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    username = os.getenv("DB_USERNAME")
    password = quote_plus(os.getenv("DB_PASSWORD"))
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False