from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['DEBUG']=True
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'blog'

from app import views