# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:40:56 2016

@author: Administrator
"""

from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)