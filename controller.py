from flask_login import login_user,login_required,logout_user
from flask import render_template,request,redirect
from app import app
from models import *
from forms import *
from werkzeug.security import check_password_hash
@app.route('/') 
def home():
    return render_template('index.html',home_page_active='active',books=Book.query.all())
 
@app.route('/book/<int:book_ind>/',methods=['GET','POST'])
def book(book_ind):
    post_data=request.form
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(data=post_data)
        if form.validate_on_submit():
            contact=Comment(comment_index=book_ind,comment_name=form.full_name.data,comment_language=form.language.data,comment=form.comment.data)
            contact.save()
    return render_template('book.html',authors=Book.query.get(book_ind).author,
    titles=Book.query.get(book_ind).title,book_ind=book_ind,prices=Book.query.get(book_ind).price,
    descriptions=Book.query.get(book_ind).description,
    languages=Language.query.get(Book.query.get(book_ind).lang_id).lang,
    genres=Genre.query.get(Book.query.get(book_ind).genre_id).genre,
    publishers=Book.query.get(book_ind).publisher,paths=Book.query.get(book_ind).image_url,form=form,user=Comment.query.all())

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    post_data=request.form
    if request.method=='POST':
        form=RegisterForm(data=post_data)
        if  form .validate_on_submit():
            user=User(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data,username=form.username.data,password=form.password.data)
            user.save()
            return redirect('/login')
    return render_template('sign_up.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if request.method=='POST':  
        post_data=request.data
        form =LoginForm(data=post_data)
        if form .validate_on_submit():
            user=User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password,form.password.data):
                login_user(user)
                return redirect('/')
    return render_template('sign_in.html',form=form)

@app.route('/user_profile') 
@login_required
def user_profile():
    return render_template('user_profile.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
