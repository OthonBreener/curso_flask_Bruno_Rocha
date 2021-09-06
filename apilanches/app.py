from flask import Flask

from apilanches.ext import site, toolbar, db, cli, migrate, hooks, admin, auth

from apilanches.ext import config



def create_app():
    """
    Factory principal: Cria um app e retorna um app
    """
    app = Flask(__name__)
    config.init_app(app)

    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)


    return app
