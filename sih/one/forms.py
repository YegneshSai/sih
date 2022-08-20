from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
class details(FlaskForm):
    x=StringField("x")