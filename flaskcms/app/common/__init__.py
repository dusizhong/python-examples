from flask import Blueprint

#蓝图
common = Blueprint('common', __name__,template_folder='../templates')  #static_folder='../static',

from . import views



