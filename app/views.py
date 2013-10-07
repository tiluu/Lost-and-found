from app import app
from flask import render_template

@app.route('/')
def landing():
	return render_template("landing.html")

@app.route('/lost')
def lost():
	title = 'Lost'
	item_post = [
			{'item': 'test1'},
			{'item': 'test2'},
			{'item': 'test3'}
	]
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
