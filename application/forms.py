from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Length, EqualTo, ValidationError

class OrderForm(FlaskForm):
	first_name = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=2, max=30)
                ])
	last_name = StringField('Last Name',
		validators=[
                        DataRequired(),
                        Length(min=3, max=30)
                ])
	number = StringField('Phone no.',
		validators=[
			DataRequired(),
			Length(min=5, max=20)
		])
	address = StringField('Address',
                validators=[
                        DataRequired(),
                        Length(min=5, max=140)
		])
	pizza = StringField('Pizza',
                validators=[
                        DataRequired(),
                        Length(min=5, max=140)
		])
	quantity = StringField('Quantity',
		StringField=[
			DataRequired()
		])

class StockForm(FlaskForm):
	pizza = StringField('Pizza',
                validators=[
                        DataRequired(),
                        Length(min=5, max=140)
                ])
	quantity = StringField('Quantity',
		 validators=[
                        DataRequired()
                ])
	




