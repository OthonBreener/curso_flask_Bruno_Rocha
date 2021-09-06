from flask import Blueprint, request, redirect
from flask import render_template #função para renderizar os templates
from flask import current_app
from flask.helpers import url_for

from apilanches.ext.auth.form import UserForm
from apilanches.ext.auth.model import User
from apilanches.ext.auth.controller import create_user, save_user_foto
from apilanches.ext.db import db 


bp = Blueprint("site", __name__) # instância do blueprint

@bp.route("/")
def index():
    current_app.logger.debug("dentro de index")
    return render_template("index.html")

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

@bp.route("/cadastro", methods=["GET","POST"])
def signup():
    import ipdb
    
    form = UserForm()
    #verifica se estamos no request method post ou get, etc. O metodo validate_on_submit
    #passa para dentro do if apenas se os dados definidos na classe auth/form.py 
    #forem satisfeitos.
    if form.validate_on_submit():
        #user = User(email=form.email.data, senha=form.senha.data)
        #db.session.add(user)
        #db.session.commit()
        #ipdb.set_trace()
        create_user(email=form.email.data,senha=form.senha.data, admin=form.admin.data)
        foto = request.files.get('foto')
        if foto:
            save_user_foto(foto.filename, foto)
            
        #forçar o login
        return redirect("/")
        
    return render_template("userform.html", form=form)