# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:25:49 2016

@author: Administrator
"""

from flask import Blueprint
auth = Blueprint('auth',__name__)
from . import views