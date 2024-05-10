from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
# from flask_wtf.recaptcha import RecaptchaField
# from email_validator import validate_email, EmailNotValidError


class Registration(FlaskForm):
    firstname = StringField("Firstname", validators=[
                            DataRequired(), Length(max=20, min=2)])
    lastname = StringField("Lastname", validators=[
        DataRequired(), Length(max=20, min=2)])

    email = StringField("Email", validators=[
        DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign up")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already Taken!")


class Login(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
