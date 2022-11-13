from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


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
    valor = FloatField('Valor do Lanche', validators=[
                       DataRequired(message='Somente números')])
    ingrediente = TextAreaField('Ingrediente', validators=[DataRequired()])


class RemoverLancheForm(FlaskForm):
    id_lanche = HiddenField()
    nome = StringField('Nome do Lanche', )
    valor = FloatField('Valor do Lanche')
    ingrediente = TextAreaField('Ingrediente')


class PorcaoConsultaForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Nome', 'Id'])


class PorcaoForm(FlaskForm):
    id_Porcao = HiddenField()
    nome = StringField('Nome da Porção', validators=[DataRequired()])
    valor = FloatField('Valor da Porção', validators=[
                       DataRequired(message='Somente números')])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    

class RemoverPorcaoForm(FlaskForm):
    id_Porcao = HiddenField()
    nome = StringField('Nome da Porção')
    valor = FloatField('Valor da Porção')
    descricao = TextAreaField('Descrição')
