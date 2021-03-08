from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired


class NewServer(FlaskForm):
    name = StringField("Frendly Name", validators=[DataRequired()])
    region = RadioField(
        "Server Region",
        validators=[DataRequired()],
        choices=[(1, "nyc1"), (2, "nyc2")],
        default=1,
    )
    size = RadioField(
        "Server Size",
        validators=[DataRequired()],
        choices=[(1, "small"), (2, "medium"), (3, "large")],
        default=1,
    )
    image = SelectField(
        "Image", validators=[DataRequired()], choices=["Ubuntu", "Fedora"]
    )
    submit = SubmitField("Build")