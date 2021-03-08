from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewServer(FlaskForm):
    name = StringField("Frendly Name", validators=[DataRequired()])
    submit = SubmitField("Build")