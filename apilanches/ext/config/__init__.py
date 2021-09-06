from dynaconf import FlaskDynaconf

def init_app(app):
    #O dynaconf busca por padrão um arquivo chamado settings,
    #bastando chamar o FlaskDynaconf com o app.
    FlaskDynaconf(app)
    #app.config.load_extensions("EXTENSIONS")
