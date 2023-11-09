from flask import Blueprint
from flask_oauthlib.provider import OAuth2Provider
from .. import app



#蓝图
oauth2Server = Blueprint('oauth2Server', __name__,template_folder='../templates')  #static_folder='../static',

oauth = OAuth2Provider(app)

from . import views