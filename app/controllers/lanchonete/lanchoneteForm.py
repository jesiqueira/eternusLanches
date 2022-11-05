from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

class MesasForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Números', 'Teste'])

class MesaNovaForm(FlaskForm):
    id_mesa = HiddenField()
    numero = IntegerField('Número da mesa', validators=[DataRequired(message='Somente número é permitido.')])