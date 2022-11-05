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
    nome = StringField('Nome do Lanche', validators=[DataRequired()])
    valor = FloatField('Valor do Lanche', validators=[
                       DataRequired(message='Somente números')])
    ingrediente = TextAreaField('Ingrediente', validators=[DataRequired()])
