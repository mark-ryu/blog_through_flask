from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        check_user_duplicate = User.query.filter_by(username=username.data).first()
        if check_user_duplicate:
            raise ValidationError('That Username is taken. Please Choose another Username')

    def validate_email(self, email):
        check_email_duplicate = User.query.filter_by(email=email.data).first()
        if check_email_duplicate:
            raise ValidationError('That Email is taken. Please Choose another Email')

class LoginForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me') 
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            check_user_duplicate = User.query.filter_by(username=username.data).first()
            if check_user_duplicate:
                raise ValidationError('That Username is taken. Please Choose another Username')

    def validate_email(self, email):
        if email.data != current_user.email:
            check_email_duplicate = User.query.filter_by(email=email.data).first()
            if check_email_duplicate:
                raise ValidationError('That Email is taken. Please Choose another Email')

