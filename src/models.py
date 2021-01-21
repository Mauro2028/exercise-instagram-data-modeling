import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email=Column(String(250),nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name=Column(String(250),nullable=False)
    password=Column(String(250),nullable=False)

    post=relationship("Post", backref="user")
    comment=relationship("Comment",backref="user")
    post_like=relationship("Post_Like",backref="user")
    def to_dict(self):
        return{}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id=Column(String(250),ForeignKey("user.id"))
    image_url=Column(String(250),nullable=False)
    date_published=Column(String(250),nullable=False)
    content=Column(String(250),nullable=False)
    longitude=Column(String(250),nullable=False)
    comments=Column(String(250),nullable=False)

    def to_dict(self):
        return {}


class PostLike(Base):
    __tablename__="postlike"
    id=Column(Integer,primary_key=True)
    post_id=Column(Integer,ForeignKey("post.id"))
    user_id=Column(Integer,ForeignKey("user.id"))

    def to_dict(self):
        return {}


class Comment(Base):
    __tablename__="comment"
    id=Column(Integer,primary_key=True)
    post_id=Column(Integer,ForeignKey("post.id"))
    post=Column(String(250),nullable=False)
    user_id=Column(Integer)
    likes=relationship("CommentLike",backref="comment")
    
    def to_dict(self):
       return {}

class CommentLike(Base):
    __tablename__="comment_like"
    id= Column(Integer,primary_key=True)
    comment_id=Column(Integer,ForeignKey("comment.id"))
    user_id=Column(Integer,ForeignKey("user.id"))

    def to_dict(self):
        return{}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')