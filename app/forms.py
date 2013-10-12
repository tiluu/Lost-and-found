from flask.ext.wtf import Form 
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import Required

class PostItem(Form):
	item_name = TextField('Item', validators=[Required()])
	descrip = TextField('Description', validators=[Required()])
	item_status = SelectField('Location', choices=[('lost', 'Lost'),('found','Found')], validators=[Required()])
	location = TextField('Location', validators=[Required()])