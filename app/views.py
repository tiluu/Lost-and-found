from app import app, db, models
from flask import render_template
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
	item_post = models.Items.query.all()
	return render_template("lost.html", 
							item_posts = item_post,
							title = title)

@app.route('/found')
def found():
	title = 'Found'
	item_post = [
			{'item': 'test1'},
			{'item': 'test2'},
			{'item': 'test3'}
	]
	return render_template("lost.html", 
							item_posts = item_post,
							title = title)

@app.route('/item')
def item():
	return render_template("items.html")