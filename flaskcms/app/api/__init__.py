from flask import Blueprint
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api
from .. import app

#蓝图
api = Blueprint('api', __name__,template_folder='../templates')  #static_folder='../static',

auth = HTTPBasicAuth(app)
apiRest = Api(app)

from . import views,models,resourceViews