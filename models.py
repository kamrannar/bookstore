from flask_login import UserMixin
from extensions import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class Genre(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    genre=db.Column(db.String(20),unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

class Language(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    lang=db.Column(db.String(20),unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30),nullable=True,unique=True)
    author=db.Column(db.String(30),nullable=True)
    price=db.Column(db.String(10),nullable=True)
    genre_id=db.Column(db.Integer,db.ForeignKey('genre.id'))
    description=db.Column(db.Text(),nullable=False)
    image_url=db.Column(db.String(400),nullable=True)
    stock=db.Column(db.Integer,nullable=True)
    lang_id=db.Column(db.Integer,db.ForeignKey('language.id'))
    publisher=db.Column(db.String(30),nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    comment_name=db.Column(db.String(30),nullable=True)
    comment=db.Column(db.String(30),nullable=True)
    comment_language=db.Column(db.String(20))
    comment_index=db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self,comment_name,comment,comment_language,comment_index) :
        self.comment=comment
        self.comment_index=comment_index
        self.comment_language=comment_language
        self.comment_name=comment_name
        
    def save(self):
        db.session.add(self)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    first_name=db.Column(db.String(30),nullable=False)
    last_name=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    username=db.Column(db.String(30),nullable=False)
    password =db.Column(db.String(255),nullable=False)
    is_active=db.Column(db.Boolean(),nullable=False)
    is_superuser=db.Column(db.Boolean(),nullable=False)

    def __init__(self,first_name,last_name,email,username,password,is_active=True,is_superuser=False) :
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.username=username
        self.password=generate_password_hash(password)
        self.is_active=is_active
        self.is_superuser=is_superuser
    
    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()
