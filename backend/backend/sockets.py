from backend import socketio,app
from flask_socketio import send,emit,join_room,leave_room
from backend.utils import validator
from flask import request
from .db import Group;

@socketio.on("join_public")
def handle_anony_join(message):
	emit("anonymous_join",message,broadcast=True)

@socketio.on("anony_message")
def handle_anony_mess(data):
	print("the data is ",data)
	return "success",200



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



@socketio.on("join")
@validator
def on_join(current_user,room_data):
	# should check whether the room exists
	room=room_data["room"]
	user=current_user
	join_room(room)
	emit("joined_room",{user},room=room)
@socketio.on("leave")
@validator
def on_leave(current_user):
	# should check whether current user is in room
	room=data["room"]
	leave_room('room')






