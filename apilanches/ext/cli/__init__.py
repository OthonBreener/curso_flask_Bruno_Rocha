from apilanches.ext.db import db
from apilanches.ext.db import model #import para trazer os imports para a criação das tabelas
from apilanches.ext.auth.model import User
import click #biblioteca usada para capturar dados da linha de comando

def init_app(app):

    @app.cli.command()
    def create_db():
        """
        Função que inicializa um novo banco de dados.
        """
        try:
            db.create_all()
        
        except:
            print('Erro ao criar o banco de dados')
    
    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--password", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, password, admin):
        """
        Função que adiciona um novo usuário no banco de dados.
        """
        user_add = model.User(
            email=email,
            password=password,
            admin=admin
        )
        db.session.add(user_add)
        try:
            db.session.commit()
            click.echo(f"Usuário {email} criado com sucesso!")
        except:
            print(f'Erro ao cadastrar o usuário {email}.')
    
    @app.cli.command()
    def list_users():
        users = User.query.all()
        click.echo(f'Lista de usuários cadastrados: {users}')
