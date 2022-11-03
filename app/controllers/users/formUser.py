from wsgiref import validate
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Endereço de E-mail', validators=[DataRequired(), Email(message='Verificar e-mail informado!')])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar Me')
    submit = SubmitField('Entrar')

class CadastroUsersForm(FlaskForm):
    nome = StringField('Informe seu nome', validators=[DataRequired(message='Nome é Obrigatório')])
    email = StringField('eternoLanches@eternus.com.br', validators=[DataRequired(message='Email é Obrigatório'), Email('Verificar e-mail informado')])
    password = PasswordField('Informe Senha', validators=[DataRequired(message='Campo obrigatório')])
    confirmePassword = PasswordField('Confime a senha', validators=[DataRequired(), EqualTo('password', message='As senhas não são iguais')])
    cidade = StringField('Informe sua cidade', validators=[DataRequired(message='Campo obrigatório')])
    rua = StringField('Informe a sua rua', validators=[DataRequired(message='Campo obrigatório')])
    bairro = StringField('Informe seu bairro', validators=[DataRequired(message='Campo obrigatório')])
    numero = IntegerField('Qual o número', validators=[DataRequired(message='Campo obrigatório'), ])
    cep = StringField('Informe o cep')
    submit = SubmitField('Cadastrar')

