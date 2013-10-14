from flask.ext.wtf import Form 
from wtforms import TextField, BooleanField, SelectField, TextAreaField
from wtforms.validators import Required

class PostItem(Form):
	item_name = TextField('Item', validators=[Required()])
	info_text = TextAreaField('Description', validators=[Required()],default='add content')
	item_status = SelectField('Location', choices=[('lost', 'Lost'),('found','Found')], validators=[Required()])
	location = TextField('Location', validators=[Required()])