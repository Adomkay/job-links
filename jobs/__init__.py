import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from jobs.query import lat_long_trace

server = Flask(__name__)

server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =  SQLAlchemy(server)
db.session.configure(autoflush = False)
app = dash.Dash(__name__, server = server, url_base_pathname = '/dashboard')

from dashboard_views.dashboard2 import app
import jobs.routes
