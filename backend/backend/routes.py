from flask import jsonify,request
from backend import app
from backend.utils import validator
from .db  import User,Group

@app.route("/register",methods=["POST"])
def create_user():
	# create new user 
	data=request.json
	print(data)
	created=User.new_user(data)
	# return created
	return created
@app.route("/login",methods=["POST"])
def login_user():
	data=request.json

	print(data)
	# check authenitication the generate jwt key 
	return jsonify({"msg":"success"}),200
	# raise NotImplementedError()


# private chat room
# create chatroom
@app.route("/chat/createroom")
@validator
def create_room(current_user):
	data=request.json
	group=Group.new(current_user,data)
	return group

@app.route("/chat/deleteroom/<id>")
@validator	
def delete_room(current_user,id):
	return Group.delete(current_user,id)
