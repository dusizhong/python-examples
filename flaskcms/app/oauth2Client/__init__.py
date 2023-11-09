from flask import Blueprint
from flask_oauthlib.client import OAuth
from .. import app

oauth = OAuth(app)

#蓝图
oauth2Client = Blueprint('oauth2Client', __name__,template_folder='../templates')  #static_folder='../static',


from . import views