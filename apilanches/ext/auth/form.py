import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class UserForm(FlaskForm):
    '''
    A biblioteca flask_wtf transforma esta classe em um formulário html.
    '''
    email = wtf.StringField('Email', validators=[wtf.validators.DataRequired(), wtf.validators.Email()])
    senha = wtf.PasswordField('Senha', validators=[wtf.validators.DataRequired()])
    foto = FileField("Foto")

# flask-login