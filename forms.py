from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#find more info at https://flask-wtf.readthedocs.io/en/stable/quickstart.html

class AddQuoteForm(FlaskForm):
    author = StringField('Author')
    quote = StringField('Quote')
    image = StringField('Image File Name')
    submit = SubmitField('Submit')
