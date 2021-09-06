
from flask import Markup, flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters

from apilanches.ext.auth.model import User
from apilanches.ext.db import db

#-TODO:-descrever-todos-os-model

class UserAdmin(ModelView):
    """Interface admin de Usuário"""
    
        # def format_user(self, request, user, *args):
    #     return user.email.split("@")[0]
    # column_formatters = {
    #     "email": format_user
    # }

    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }

    column_list = ["admin", "email"] #indica as listas de colunas que serão exibidas

    column_labels = {"email": "User login"}

    column_searchable_list = ["email"] #comando para permitir fazer buscas 

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email, "dominio", options=(("gmail", "Gmail"), ("hotmail", "Hotmail"), ("outlook", "Outlook"))
        ),
    ]

    can_edit = False #Definide se o usuario pode ou não editar
    can_create = True #Define se o usiario pode ou não criar
    can_delete = True #Definide se o usuario pode ou não deletar

    @action("toggle_admin", "Toggle admin status", "Are you sure?")
    def toggle_admin_status(self, ids):
        '''
        Função que modifica o status do administrador.
        '''

        #Função que faz um seletec no banco de dados e retorna todos os 
        #usuarios com o id selecionado
        users = User.query.filter(User.id.in_(ids))
        for user in users.all():
            user.admin = not user.admin
        db.session.commit()
        #flash retorna uma mensagem ao efetuar uma mudança
        flash(f"{users.count()} usuários alterados com sucesso!", "success")

    @action("send_email", "Send email to all users", "Are you sure?")
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem do email
        # 2) enviar o email
        flash(f"{len(users)} emails enviados.", "success")
    