from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class MyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    numberofbedrooms = IntegerField('No Of Bedrooms', validators=[InputRequired()])
    numberofbathrooms = IntegerField('No Of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField(u'Property Type', choices=[('House'),('Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'jpg or png images only!')])
