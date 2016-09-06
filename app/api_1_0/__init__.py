# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:24:08 2016

@author: Administrator
"""

from flask import Blueprint
api = Blueprint('api',__name__)
from . import authentication,posts,users,comments,errors