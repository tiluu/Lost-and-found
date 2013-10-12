from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from moment import moment #allows templates to call moment wrapper

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.globals['moment'] = moment #moment class now global
db = SQLAlchemy(app)



from app import views, models
