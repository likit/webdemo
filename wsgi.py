from app import create_app, admin, db
from flask_admin.contrib.sqla import ModelView


app = create_app()

from app.views import *
from app.models import Document

admin.add_views(ModelView(Document, db.session))