# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,url_for,session,redirect,flash
from flask.ext.bootstrap import Bootstrap 
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.mail import Mail,Message
import os


from flask.ext.script import Shell

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
    
    
#basedir = os.path.abspath(os.path.dirname(__file__))

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

#app = Flask(__name__)
#bootstrap = Bootstrap(app)
#moment = Moment(app)
#manager = Manager(app)
#mail = Mail(app)
manager.add_command('shell',Shell(make_context=make_shell_context))
#app.config['SECRET_KEY'] = 'eellkk'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
#app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
#app.config['MAIL_USE_TLS'] = True
#app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
#app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin eellkk@outlook.com'
#app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    mail.send(msg)
    
    
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role',lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>' % self.name
        
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username
  

#@app.route('/',methods=['GET','POST'])
#def index():
#    form = NameForm()
#    if form.validate_on_submit():
#        user = User.query.filter_by(username=form.name.data).first()
#        if user is None:
#            user = User(username=form.name.data)
#            db.session.add(user)
#            session['Known']=False
#            if app.config['FLASKY_ADMIN']:
#                send_email(app.config['FLASKY_ADMIN'],'New user','mail/new_user',user=user)
#        else:
#            session['Known']=True
#        session['name']=form.name.data
#        form.name.data=''                
#        return redirect(url_for('index'))
#    return render_template('index.html',current_time=datetime.utcnow(),name=session.get('name'),form=form,known=session.get('Known',False))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
    


#if __name__ == '__main__':
#    manager.run()

