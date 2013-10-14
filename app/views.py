from app import app, db, models
from flask import render_template, redirect, request
from forms import *
from models import *
import datetime
import re
import unidecode 


def slugify(str):
	str = unidecode.unidecode(str).lower()
	return re.sub(r'\W+', '-', str)


@app.route('/')
def landing():
	return render_template("landing.html")

@app.route('/lost')
def lost():
	title = 'Lost'
	item_post = models.Items.query.filter_by(item_status='lost')
	return render_template("lost.html", 
							item_posts = item_post,
							title = title)

@app.route('/found')
def found():
	title = 'Found'
	item_post = models.Items.query.filter_by(item_status='found')
	return render_template("lost.html", 
							item_posts = item_post,
							title = title)

@app.route('/item')
def item():
	item_param = request.args.get('id','item_id')
	title = 'Item #' + item_param
	item_post = models.Items.query.filter_by(id=item_param) 
	return render_template("items.html", 
							item_posts =item_post,
							title = title)

@app.route('/add', methods = ['GET', 'POST'])
def add():
	title = "Post Item"
	form = PostItem()
	if form.validate_on_submit():
		post = Items(name_item = form.item_name.data,description=form.descrip.data, 
					date=datetime.datetime.utcnow(), item_status=form.item_status.data,
					area=form.location.data)
		db.session.add(post)
		db.session.commit()

		return redirect(form.item_status.data)

	return render_template("add.html", 
						title = title, 
						form = form)









