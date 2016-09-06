# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:40:40 2016

@author: Administrator
"""
from functools import wraps
from flask import g
from .errors import forbidden

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args,**kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient Permissions')
            return f(*args,**kwargs)
        return decorated_function
    return decorator