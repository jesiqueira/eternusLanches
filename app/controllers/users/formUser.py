from wsgiref import validate
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, Email

class LoginForm(FlaskForm):
    login = StringField('Endereço de E-mail', validators=[DataRequired(), Email(message='Verificar e-mail informado!')])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar Me')
    submit = SubmitField('Entrar')
