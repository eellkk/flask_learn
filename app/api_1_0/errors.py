# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:35:52 2016

@author: Administrator
"""
from flask import jsonify
from . import api
from app.exceptions import ValidationError

def bad_request(message):
    response = jsonify({'error':'bad request','message':message})
    response.status_code = 400
    
def unauthorized(message):
    response = jsonify({'error':'unauthorized','message':message})
    response.status_code = 401
    

def forbidden(message):
    response = jsonify({'error':'forbidden','message':message})
    response.status_code = 403
    return response
    
@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])