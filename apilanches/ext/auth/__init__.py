from flask_admin import Admin
from apilanches.ext.auth import model
from apilanches.ext.auth.admin import UserAdmin
from flask_admin.contrib.sqla import ModelView
from apilanches.ext.auth.commands import add_user, list_users
from apilanches.ext.admin import admin
from apilanches.ext.auth.model import User
from apilanches.ext.db import db

def init_app(app):
    """TODO: inicializar Flask Simple Login + JWT"""

    app.cli.command()(list_users)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))
    #admin.add_view(ModelView(User, db.session))