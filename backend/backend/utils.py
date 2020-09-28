from email_validator import validate_email,EmailNotValidError

from flask import request
from . import bcrypt

import uuid
from functools import wraps
from .config import SECRET_KEY
import jwt
import datetime

def test_import():
	return True

def chatter(func):
	@wraps(func)
	def inner_function(*args,**kwargs):
		data=request.json
		print("the details are",request.args)
		try:
			username=data["username"]

		except Exception as e:
			username=None
		return func(username,*args,**kwargs)
	return inner_function
def validator(func):
	@wraps(func)
	def inner_function(*args,**kwargs):
	
		token=request.args.get("auth_key")

		from backend.db import User
		

		try:
			token=request.args.get("auth_key")
			if token is None:
				return "authentication failed",401
			user_email=jwt_validator(token)
			user_email=user_email.get("data")
			current_user=User.get_user(user_email)
			print("current_user is ",current_user)

		except Exception as e:
			print(e)
			# print("raised excepttio here ")
			return "authentication failed",401

		return func(current_user,*args,**kwargs)

	return inner_function
def isEmail(email):
	try:
		valid=validate_email(email)
	except EmailValidError as e:
		return False
	return True

def  password_hash(pwd):
	try:
		hashed=bcrypt.generate_password_hash(pwd)
	except Exception as e:
		raise e
	return hashed

def validate_password(pwd,hashed):

	return bcrypt.check_password_hash(hashed,pwd)
def uuid_generator():
	return str(uuid.uuid4())
	
def email_verification(email):
	raise NotImplementedError()
def jwt_generator(email):
	encoded = jwt.encode({'data':email,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=15)},SECRET_KEY,algorithm='HS256')
	return encoded.decode("utf-8")

def jwt_validator(auth_token):
	try:
		user_email=jwt.decode(auth_token,SECRET_KEY,algorithm="HS256")
	except Exception as e:
		print(str(e))
		raise e

	return user_email
	

def saltify(items):
	store=[{"public_id":item.public_id,"name":item.group_name} for item in items]
	return store
