from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))


    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __init__(self,username,password,email):
        self.username=username
        self.set_password(password)
        self.email=email

    def __repr__(self):
        return "<User> {}".format(self.username)



class Province(db.Model):
    __tablename__="provinces"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    districts=db.relationship("District",backref="province",lazy="dynamic")

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return "<Province> {}".format(self.name)


class District(db.Model):
    __tablename__="districts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    province_id=db.Column(db.Integer,db.ForeignKey('provinces.id'))

    localbodies=db.relationship("LocalBody",backref="district",lazy="dynamic")

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return "<District> {}".format(self.name)


class LocalBody(db.Model):
    __tablename__="localbodies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    type=db.Column(db.String(64))

    def __init__(self,name):
        self.name=name

    district_id=db.Column(db.Integer,db.ForeignKey('districts.id'))

    def __repr__(self):
        return "<Local Body> {}".format(self.name)

class Ward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ward_no=db.Column(db.String(64), index=True)