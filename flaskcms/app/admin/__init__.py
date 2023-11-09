from flask import Blueprint

#蓝图
admin = Blueprint('admin', __name__,template_folder='../templates')  #static_folder='../static',

from . import views