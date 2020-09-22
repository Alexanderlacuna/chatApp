from backend  import database as db;
from .utils import uuid_generator,password_hash

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	public_id=db.Column(db.String(120),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	password=db.Column(db.String(120),unique=False,nullable=False)
	comments=db.relationship("Comment",backref="creator",lazy=True)
	groups=db.relationship("Group",backref="members",lazy=True)

	@staticmethod
	def new_user(**kwargs):
		try:
			email=kwargs.get(email)
			public_id=uuid_generator()
			password=kwargs.get(password)
			hash_pwd=password_hash(password)
			user=User(email,public_id,password)
			db.session.add(user)
			db.session.commit()

		except Exception as e:
			return "Error creating user",401

		return "successfully created",201


	def user_exists(self,email,pwd):
		raise NotImplementedError()
	

	def __repr__(self):
		return f'user is {self.email} and public id {self.public_id}'
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

	@staticmethod
	def new(current_user,**kwargs):
		public_id=uuid_generator()
		name=kwargs.get("group_name")
		creator=current_user

		try:
			user=Group(public_id,group_name=name,group_creator=creator)
			db.session.add(user)
			db.session.commit()

		except Exception as e:
			return str(e),403
		return "successfully created group",201

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