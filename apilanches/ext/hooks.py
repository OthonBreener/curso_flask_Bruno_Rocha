#from apilanches.ext.db import db

def init_app(app):
    @app.before_first_request
    def init_everthing():
        print("Isto roda antes do primeiro request!")