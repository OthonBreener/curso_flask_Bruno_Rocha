from apilanches.ext.db import db

class User(db.Model):
    '''
    Classe que representa o usuário no banco de dados, caso admin seja True
    esse usuário tem permissão para administrar o site.
    '''
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.Unicode, unique=True)
    senha = db.Column('senha', db.Unicode)
    admin = db.Column('admin', db.Boolean)

    def __repr__(self):
        '''
        Função que muda o atributo que representa a classe.
        '''
        return self.email 



    