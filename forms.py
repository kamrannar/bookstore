from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,Email

class ContactForm(FlaskForm):
    full_name=StringField('Tam adınız :', validators=[DataRequired(),Length(min=5,max=100) ])
    comment=TextAreaField('Şərhiniz :', validators=[DataRequired()])
    language=SelectField('Hansı dildə oxumusunuz ?',choices=['Azərbaycanca','Ingiliscə'])
    read=SelectField('Bu kitabı oxumusunuzmu ?',choices=['Oxumuşam','Oxumamışam'])

class RegisterForm(FlaskForm):
    first_name=StringField('Ad :', validators=[DataRequired(),Length(min=3,max=30) ])
    last_name=StringField('Soyad :', validators=[DataRequired(),Length(min=3,max=30) ])
    email=StringField('Email :', validators=[DataRequired(),Email(),Length(min=3,max=30) ])
    username=StringField('İstifadəçi adı :', validators=[DataRequired(),Length(min=3,max=30) ])
    password=StringField('Şifrə :', validators=[DataRequired(),Length(min=8,max=30) ])

class LoginForm(FlaskForm):
    username=StringField('İstifadəçi adı :', validators=[DataRequired(),Length(min=3,max=30) ])
    password=StringField('Şifrə :', validators=[DataRequired(),Length(min=8,max=30) ])