# from flask  import Flask,render_template
from flask_socketio import SocketIO
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
bcrypt=Bcrypt(app)
app.config.from_pyfile("config.py")
database=SQLAlchemy(app)
socketio=SocketIO(app, cors_allowed_origins="*")
from .utils import validator
from .db import User
from .sockets import *;
from .routes import *;


