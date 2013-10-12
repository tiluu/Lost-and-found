from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(64), index = True)
	contact = db.Column(db.String(120), index = True, unique=True)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	posts = db.relationship('Items', backref = 'user', lazy = 'dynamic')
	
	def __repr__(self):
		return '<User %r>' % (self.user_name)

class Items(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name_item = db.Column(db.String(100), index = True)
	description = db.Column(db.String(500))
	date = db.Column(db.DateTime)
	item_status = db.Column(db.String(10), index = True)
	area = db.Column(db.String(100), index = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Item %r>' % (self.name_item)

