from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError

class MesasForm(FlaskForm):
    consultar = StringField('Consulta', validators=[DataRequired()])
    selection = SelectField(choices=['Números', 'Teste'])
