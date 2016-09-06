# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:46:15 2016

@author: Administrator
"""
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField,SelectField,TextAreaField
from wtforms.validators import Required,Length,Email,Regexp,ValidationError
from ..models import Role,User
from flask.ext.pagedown.fields import PageDownField

class LoginForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    email = StringField('Email',validators=[Required(),Email(),Length(1,64)])
    submit = SubmitField('Log In')
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in ')
    
class EditProfileForm(Form):
    name = StringField('Name',validators=[Length(0,64)])
    location = StringField('Location',validators=[Length(0,64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    
class EditProfileAdminForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    username = StringField('Username',validators=[Required(),Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must have only letters,numbers,dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role',coerce=int)
    name = StringField('Real name',validators=[Length(0,64)])
    location = StringField('Location',validators=[Length(0,64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    
    def __init__(self,user,*args,**kwargs):
        super(EditProfileAdminForm,self).__init__(*args,**kwargs)
        self.role.choices = [(role.id,role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user
        
    def validator_email(self,field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
            
    def validator_username(self,field):
        if field.data != self.user.username and User.query.filer_by(username=field.data).first():
            raise ValidationError('Username already in use.')
            
            
class PostForm(Form):
    body = PageDownField("Whats on your mind?",validators=[Required()])
    submit = SubmitField("Submit")
    
class CommentForm(Form):
    body = StringField('',validators=[Required()])
    submit = SubmitField('Submit')
    