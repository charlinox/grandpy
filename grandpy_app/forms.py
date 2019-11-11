from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question = StringField('Bonjour, mon poussin. Tu voulais me demander quelque chose sur un lieu ?', validators=[DataRequired()])
    submit = SubmitField('Envoyer')