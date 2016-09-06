# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:09:22 2016

@author: Administrator
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'eellkk'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <eellkk@outlook.com>'
    FLASKY_ADMIN = 'eellkk@outlook.com'
    
    @staticmethod
    def init_app(app):
        pass
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'eellkk@outlook.com'
    MAIL_PASSWORD = '12261991ml'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')
    
class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TSET_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data-test.sqlite')
    
class ProductionConfig(Config):
    SQLALCHEMT_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')
    
    @staticmethod
    def init_app(cls,app):
        Config.init_app(app)
        
        
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls,'MAIL_USERNAME',None) is not None:
            credentials = (cls.MAIL_USERNAME,cls.MAIL_PASSWORD)
            if getattr(cls,'MAIL_USE_TLS',None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost =(cls.MAIL_SERVER,cls.MAIL_PORT),
            fromaddr =cls.FLASKY_MAIL_SENDER,
            toaddrs = [cls.FLASKY_ADMIN],
            subject = cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials = credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
        
        
config ={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig


}

