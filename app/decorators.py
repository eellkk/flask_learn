# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:33:24 2016

@author: Administrator
"""

from functools import wraps
from flask import abort
from flask.ext.login import current_user
from .models import Permission
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args,**kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args,**kwargs)
        return decorated_function
    return decorator
    
def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)