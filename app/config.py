import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # or your preferred database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False