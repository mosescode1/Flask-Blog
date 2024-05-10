
from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bycrypt
from flaskblog.form import Login, Registration
import datetime
from flaskblog.models import User
from flask_login import login_user
curentday = datetime.datetime.now(datetime.timezone.utc)
posts = [
    {
        "author": "Eteng Moses Efa",
        "title": "Learning Flask",
        "content": "I am very much excited right now",
        "created_at": f"{curentday.day} {curentday.year}"
    },
    {
        "author": "Eteng Ruth",
        "title": "Efa as a dedicated guy",
        "content": "He is my younger brother and i love him so much",
        "created_at": f"{curentday.day} {curentday.year}"
    },
    {
        "author": "Eteng Emmanuel",
        "title": "My Elder Bro",
        "content": "Lets Make Money And Get Those Girls ",
        "created_at": f"{curentday.day} {curentday.year}"
    },
    {
        "author": "Tems",
        "title": "Efa is my Mentee",
        "content": "A dedicated boy he is going places",
        "created_at": f"{curentday.day} {curentday.year}"
    },

]


@ app.route("/")
@ app.route("/index.html")
def home():
    return render_template('index.html', posts=posts)


@ app.route("/register.html", methods=["GET", "POST"])
def register():
    form = Registration()
    if form.validate_on_submit():  # Check if the form is submitted and valid
        hashed_password = bycrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = User(firstname=form.firstname.data, lastname=form.lastname.data,
                    email=form.email.data, password=hashed_password)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        flash(
            f'Account created for {form.firstname.data} {form.lastname.data }!', 'success')
        return redirect(url_for("login"))
    return render_template('register.html', title="Register Here", form=form)


@ app.route("/login.html", methods=["GET", "POST"])
def login():
    form = Login()
    # print(form)
    if form.validate_on_submit():  # Check if the form is submitted and valid
        user = User.query.filter_by(email=form.email.data).first()
        if user and bycrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("home"))
        else:
            flash(
                f'Enter your correct Details !', 'danger')
    return render_template('login.html', title="Login", form=form)
