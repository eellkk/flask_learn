# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 09:52:34 2016

@author: Administrator
"""
from flask import g,jsonify,request,url_for
from . import api
from ..models import Comment,Post,Permission
from .decorators import permission_required
from .. import db

@api.route('/comments/')
def get_comments():
    page = request.get('page',1,type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(page)
    comments = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_comments',page=page-1,_external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_comments',page=page+1,_external=True)
    return jsonify({
        'comments': [comment.to_json() for comment in comments],
        'prev':prev,
        'next':next,
        'count':pagination.total
    })
    
@api.route('/comments/<int:id>')
def get_comment():
    comment = Comment.query.get_or_404(id)
    return comment.to_json()
    
@api.route('/comments/<int:id>/comments')
def get_post_comments(id):
    post = Post.query.get_or_404(id)
    page = request.get('page',1,type=int)
    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(page)
    comments = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_post_comment',page=page-1,_external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_post_comment',page=page+1,_external=True)
    return jsonify({
        'comments':[comment.to_json() for comment in comments],
        'prev':prev,
        'next':next,
        'count':pagination.total
    })
    
    
@api.route('posts/<int:id>/comments',methods=['POST'])
@permission_required(Permission.COMMENT)
def new_post_comment(id):
    post = Post.query.get_or_404(id)
    comment = Comment.from_json(request.json)
    comment.author = g.current_user
    comment.post = post
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_json()),201,{'Location':url_for('api.get_comment',id=comment.id,_external=True)}