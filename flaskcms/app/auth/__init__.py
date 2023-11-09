from flask import Blueprint

#蓝图
auth = Blueprint('auth', __name__,template_folder='../templates')  #static_folder='../static',

from . import views