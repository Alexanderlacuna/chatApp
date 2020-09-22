# from flask  import Flask,render_template
from flask_socketio import SocketIO,send,emit,join_room,leave_room
from flask import Flask,render_template,request
from functools import wraps

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt




app=Flask(__name__)
bcrypt=Bcrypt(app)
app.config.from_pyfile("config.py")
database=SQLAlchemy(app)
socketio=SocketIO(app, cors_allowed_origins="*")
# socketio=SocketIO(app)

from .utils import validator
from .db import User
from .sockets import *;

@app.route("/register",methods=["POST"])
def create_user():
	data=request.json
	created=User.new_user(data)
	return created
@app.route("/login",methods=["POST"])
def login_user():
	raise NotImplementedError()

