from email_validator import validate_email,EmailNotValidError
from . import bcrypt
from functools import wraps

def test_import():
	return True
def validator(func):
	@wraps(func)
	def inner_function(*args,**kwargs):
		
		print(f'args is {args} and kwargs are {kwargs}')




		
		print("calling inner function")
		try:
			data=args[0]
			email=data["email"]
			password=data["password"]
			current_user=email or None
			# call database to validate user

			# do email and password validation
		except EmailValidError as e:
			print("error encoutered")
			return  "error"
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
	return bcrypt.check_password(hashed,pwd)



def uuid_generator():
	# return str(uuid.uu)
	raise NotImplementedError()

def email_verification(email):
	# assert is email the verify
	raise NotImplementedError()


def jwt_generator(email):
	raise NotImplementedError()

def jwt_validator(jwt):
	raise NotImplementedError()
