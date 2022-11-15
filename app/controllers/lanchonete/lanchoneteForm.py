from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField, IntegerField, FloatField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed


class MesasForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Números', 'Teste'])


class MesaNovaForm(FlaskForm):
    id_mesa = HiddenField()
    numero = IntegerField('Número da mesa', validators=[
                          DataRequired(message='Somente número é permitido.')])


class LancheConsultaForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Nome', 'Id'])


class LancheForm(FlaskForm):
    id_lanche = HiddenField()
    nome = StringField('Nome do Lanche', validators=[DataRequired()])
    valor = FloatField('Valor do Lanche', validators=[DataRequired(message='Somente números')])
    ingrediente = TextAreaField('Ingrediente', validators=[DataRequired()])
    imagem = FileField('Imagem do Lanche', validators=[FileAllowed(['jpg', 'jpeg', 'png'], message='Somente formatos: jpg, png são permitidas.')])

class RemoverLancheForm(FlaskForm):
    id_lanche = HiddenField()
    nome = StringField('Nome do Lanche', )
    valor = FloatField('Valor do Lanche')
    ingrediente = TextAreaField('Ingrediente')
    imagem = FileField('Imagem do Lanche', validators=[FileAllowed(['jpg', 'jpeg', 'png'], message='Somente formatos: jpg, png são permitidas.')])


class PorcaoConsultaForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Nome', 'Id'])


class PorcaoForm(FlaskForm):
    id_Porcao = HiddenField()
    nome = StringField('Nome da Porção', validators=[DataRequired()])
    valor = FloatField('Valor da Porção', validators=[DataRequired(message='Somente números')])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    imagem = FileField('Imagem da Porção', validators=[FileAllowed(['jpg', 'jpeg', 'png'], message='Somente formatos: jpg, png são permitidas.')])
    

class RemoverPorcaoForm(FlaskForm):
    id_Porcao = HiddenField()
    nome = StringField('Nome da Porção')
    valor = FloatField('Valor da Porção')
    descricao = TextAreaField('Descrição')
    imagem = FileField('Imagem da Porção', validators=[FileAllowed(['jpg', 'jpeg', 'png'], message='Somente formatos: jpg, png são permitidas.')])


class BebidaConsultaForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Nome', 'Id'])


class BebidaForm(FlaskForm):
    id_Porcao = HiddenField()
    nome = StringField('Nome da bebida', validators=[DataRequired()])
    valor = FloatField('Valor da bebida', validators=[DataRequired(message='Somente números')])
    imagem = FileField('Imagem do suco', validators=[FileAllowed(['jpg', 'jpeg', 'png'], message='Somente formatos: jpg, png são permitidas.')])
    alcoolica = BooleanField('Bebida alcoólica')
