# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:46:15 2016

@author: Administrator
"""
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError,TextField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from ..models import User


class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Email(),Length(1,64)])    
    password = PasswordField('Password',validators=[Required()])
    submit = SubmitField('Log In')
    remember_me = BooleanField('Keep me logged in ')
    
    
class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Email(),Length(1,64)])
    username = StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z]*$',0,'Usernames must have only letters,numbers,dots or underscores')])
    password = PasswordField('Password',validators=[Required(),EqualTo('password2',message='Passwords must match.')])
    password2 = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Register')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
            
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
    
