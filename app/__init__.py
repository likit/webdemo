import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_admin import Admin
from flask_migrate import Migrate

load_dotenv()

db = SQLAlchemy()
admin = Admin()
migration = Migrate()

from .models import Document


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    db.init_app(app)
    migration.init_app(app, db)
    admin.init_app(app)
    return app
