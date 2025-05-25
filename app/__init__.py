from flask import Flask
from .models.entities import db, ma, migrate

from os import getenv
from dotenv import load_dotenv

load_dotenv()
database_url = getenv("DATABASE_URL")
secret_key = getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_url}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = f"{secret_key}"

ma.init_app(app)
db.init_app(app)
migrate.init_app(app, db)

@app.shell_context_processor
def create_shell_context():
    return dict(
        app=app,
        db=db,
        ma=ma,
        migrate=migrate
    )