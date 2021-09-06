import click

from apilanches.ext.auth.model import User
from apilanches.ext.auth.controller import create_user
from apilanches.ext.db import db


def list_users():
    users = User.query.all()
    click.echo(f"lista de usuarios {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, senha, admin):
    """adiciona novo usuario"""
    #TODO tradatar a excessão caso o usuário já exista
    create_user(email=email, senha=senha, admin=admin)

    click.echo(f"Usuário {email} criado com sucesso!")