from os import  urandom
DEBUG=True
SQLALCHEMY_DATABASE_URI="sqlite:////tmp/test.db"

SQLALCHEMY_TRACK_MODIFICATIONS=False


SECRET_KEY=str(urandom(16))
# print("Dwe")