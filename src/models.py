import os
import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er # type: ignore

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False)
    firstname = Column(String(200), nullable=False)
    lastname = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)


    followers_to= relationship("Follower")
    followers_from = relationship("Follower")
    post = relationship("Post")


class Follower(Base):
    __tablename__ = 'follower'
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=True)

    user= relationship("User")
    

    

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)

    post = relationship("Post")
    author = relationship("User")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False) 
    url = Column(String(100), nullable=False)

    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    post_text = Column(String(100), nullable=False)

    user = relationship("User")
    comments = relationship("Comment")
    media = relationship("Media")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
