from flask_migrate import Migrate
from apilanches.ext.db import model, db # noqa

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)
