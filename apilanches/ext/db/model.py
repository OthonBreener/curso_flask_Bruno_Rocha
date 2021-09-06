from enum import unique
from apilanches.ext.db import db

class Category(db.Model):
    '''
    Classe que representa um tipo de categoria, por exemplo pizza ou sanduiche.
    São categorias unicas que não podem ter duas iguais.
    '''
    __tablename__ = "category"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode, unique=True)
    #classe adicionada depois para testar o migrate
    on_menu = db.Column('on_menu', db.Boolean)

class Store(db.Model):
    '''
    Classe que representa uma loja no geral.
    No nosso caso, vai representar as lanchonetes.
    '''
    __tablename__ = "store"
    id =db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
    active = db.Column('active', db.Boolean)

    user = db.relationship('User', foreign_keys = user_id)
    category = db.relationship('Category', foreign_keys = category_id)

class Items(db.Model):
    '''
    Classe que representa os items do cardapio
    '''
    __tablename__ = "items"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    image = db.Column('image', db.Unicode)
    price = db.Column('price', db.Numeric)
    available = db.Column('available', db.Boolean)


    store_id = db.Column('store_id', db.Integer, db.ForeignKey('store.id'))

    store = db.relationship('Store', foreign_keys=store_id)

class Order(db.Model):
    '''
    Classe que representa um pedido efetuado pelo cliente
    '''
    __tablename__ = "order"

    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))
    address_id = db.Column("address_id", db.Integer, db.ForeignKey("address.id"))

    user = db.relationship("User", foreign_keys=user_id)
    store = db.relationship("Store", foreign_keys=store_id)
    address = db.relationship("Address", foreign_keys=address_id)


class OrderItems(db.Model):
    '''
    Classe que representa os itens contidos no pedido do cliente.
    '''
    __tablename__ = "order_items"

    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    items_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))

    quant = db.Column("quant", db.Integer)
    id = db.Column("id", db.Integer, primary_key=True)

    order = db.relationship("Order", foreign_keys=order_id)
    items = db.relationship("Items", foreign_keys=items_id)


class Checkout(db.Model):
    __tablename__ = "checkout"

    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    order = db.relationship("Order", foreign_keys=order_id)


class Address(db.Model):
    __tablename__ = "address"

    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zip", db.Unicode)
    country = db.Column("country", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", foreign_keys=user_id)


