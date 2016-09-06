# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 09:14:20 2016

@author: Administrator
"""

from flask import url_for,current_app,jsonify,request
from ..models import User,Post
from . import api

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())
    
@api.route('/users/<int:id>/posts/')
def get_user_posts(id):
    user = User.query.get_or_404(id)
    page = request.get('page',1,type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(page)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_posts',page=page-1,_external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_posts',page=page+1,_external=True)
        
    posts = Post.query.filter(author_id=id).all()
    return jsonify({
        'posts':[post.to_json() for post in posts],
        'prev':prev,
        'next':next,
        'count':pagination.total
    })
    
    
@api.route('/users/<int:id>/timeline/')
def get_user_followed_posts(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page',1,type=int)
    pagination = user.followed_posts.order_by(Post.timestamp.desc()).paginate(page)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_followed_posts',page=page-1,_external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_followed_posts',page=page+1,_external=True)
    return jsonify({
        'post':[post.to_json() for post in posts],
        'prev':prev,
        'next':next,
        'count':pagination.total
    })
    