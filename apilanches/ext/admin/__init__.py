from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from apilanches.ext.auth.admin import UserAdmin
from apilanches.ext.auth.model import User as usuario
from apilanches.ext.db import db
from apilanches.ext.db.model import Category

admin = Admin()

def init_app(app):
    #ele vai tentar pegar o nome do dynacong, se não conseguir vai usar LanchesIbia
    admin.name = app.config.get("APPNAME", "LanchesIbia")
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    #Proteger com senha

    admin.add_view(UserAdmin(usuario, db.session, endpoint="users_"))
    admin.add_view(ModelView(Category, db.session))
