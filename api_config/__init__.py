from flask import (
    Flask,
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask('MyApp')
CORS(app)

#configuracion de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:andres@localhost:5433/postgres"  # noqa
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)