import os

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import current_app as app
from apilanches.ext.auth.model import User
from apilanches.ext.db import db
# generate_password_hash: pega um texto puro e transforma em um algoritmo encriptado
# check_password_hash: verifica se o algoritmo encriptado é igual ao valor que já temos

ALG = "pbkdf2:sha256"

def create_user(email: str, senha:str, admin:bool = False) -> User:
    senha = generate_password_hash(senha, ALG)
    user = User(email=email, senha=senha, admin = admin)
    db.session.add(user)
    # tratar excessão caso já exista o usuarip
    db.session.commit()
    return user 

def save_user_foto(filename, filestorage):
    '''
    Salva a foto do usuário em:
    ./uploads
    '''
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"], 
        secure_filename(filename)
    )
    filestorage.save(filename)


def save(user):
    '''
    Função que salva um novo usuário no banco de dados.
    '''
    user = User()
    db.session.add(user)
    db.session.commit()