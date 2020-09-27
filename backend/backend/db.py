from backend  import database as db;
from .utils import uuid_generator,password_hash,isEmail,validate_password,saltify
from flask import jsonify
class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	public_id=db.Column(db.String(120),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	password=db.Column(db.String(120),unique=False,nullable=False)
	comments=db.relationship("Comment",backref="creator",lazy=True)
	groups=db.relationship("Group",backref="members",lazy=True)



	@staticmethod
	def new_user(data):
		print("the data  is",data)
		try:
			email=data.get("email")
			if isEmail(email):
				pass
			else:
				return "valid email is required",401
			
			password=data.get("password")
			hash_pwd=password_hash(password)
			public_id=uuid_generator()
			user=User(email=email,public_id=public_id,password=hash_pwd)
			db.session.add(user)
			db.session.commit()

		except Exception as e:
			print(str(e))
			return "Invalid details or user already exists",401

		return "successfully created",201


	def user_exists(email,pwd):
		print("the email calling is",email)
		user=User.query.filter_by(email=email).first()
		print("the user found calling is ",user)
		if user is not None:
			return validate_password(pwd,user.password)
		return False



	def get_user(email):
		print("call with email")
		user=User.query.filter_by(email=email).first()
		# print("details are ", {email:user.email,public_id:user.public_id})
		print("the user is",user)
		# print("the user id ",user.public_id)
		try:
			found_user={
			"email":user.email,
			"public_id":user.public_id

			}
		except Exception as e:
			raise e

		return found_user

		
		
	

	def __repr__(self):
		# return {public_id:self.public_id,email:self.email}
		return f'{self.public_id}->{self.email}'
class  Comment(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	post=db.Column(db.Text,unique=False,nullable=True)
	creator_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
	@staticmethod
	def create_comment():
		raise NotImplementedError()





class Group(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	public_id=db.Column(db.String(120),nullable=False,unique=True)
	group_name=db.Column(db.String(120),nullable=False)
	group_creator=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

	def __repr__(self):
		return f"{self.public_id}->{self.group_name}"

    # def saltify(groups):
    # 	store=[]
    # 	for group  in groups:
    # 		item={id:group.group_name,name:group_name}
    # 		store.append(item)

    # 	return stor



	@staticmethod
	def new(current_user,data):
		print("calling specific function")
		public_id=uuid_generator()
		name=data.get("items")
		creator=current_user
		print("The name is ",name)
        
		try:
			user=User.query.filter_by(email=current_user.get("email")).first();


			group=Group(public_id=public_id,group_name=name,group_creator=user.id)
			
			db.session.add(group)
			db.session.commit()

		except Exception as e:
			# print("the excepttion is",str(e))
			print(str(e))
			return "Could not create group",403
			# return str(e),403

		group=Group.query.filter_by(public_id=public_id);
		return jsonify(saltify(group)),201
		# return "successfully created group",201

	@staticmethod
	def get_all():
		groups=Group.query.all()
		if len(groups)<1:
			return "no group exists",401

		return jsonify(saltify(groups)),200

	@staticmethod
	def delete(current_user,group_id):
		# check whether current user createt the group

		try:
			to_delete=Group.filter_by(id=group_id).first()
			db.session.remove(to_delete)
			
		except Exception as e:
			return f'failed to delete group {group_id}'


		return "successfully deleted group",200
		







	# should include creator id and members