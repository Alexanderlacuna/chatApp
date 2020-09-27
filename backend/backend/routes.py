from flask import jsonify,request,redirect,url_for
from backend import app
from backend.utils import validator,jwt_generator
from .db  import User,Group


@app.route("/test",methods=["POST"])
@validator
def test(current_user):

	return "yes"
@app.route("/register",methods=["POST"])
def create_user():
	# create new user 
	data=request.json
	created=User.new_user(data)
	if created[1]==401:
		return created
	return jwt_generator(data["email"]),201
@app.route("/login",methods=["POST"])
def login_user():

	# should also check email validity
	data=request.json
	print("The data received is",data)
	try:
		email=data.get("email")
		password=data.get("password")

	except Exception as e:
		return jsonify({"data":"Auth details are required"}),401

	# print("the email add password",email,password)
	# return {"data":"sucess"},200


	# email=data.get("email")
	# pwd=data.get("password")
	exists=User.user_exists(email=email,pwd=password)


	if (exists):
		# should return auth key 
		email=data.get("email")
		return jsonify({"auth_key":jwt_generator(email)}),200
		

	return {"msg":"invalid login details"},401
	

# private chat room
# create chatroom
@app.route("/chat/createroom",methods=["POST"])
@validator
def create_room(current_user):
	data=request.json
	group=Group.new(current_user,data)
	return group

@app.route("/chat/deleteroom/<id>")
@validator	
def delete_room(current_user,id):
	return Group.delete(current_user,id)


@app.route("/getrooms",methods=["GET"])
def get_all():
	print("function to get rooms called")
	return Group.get_all()