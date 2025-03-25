from flask import Blueprint

#蓝图
blog = Blueprint('blog', __name__,template_folder='../templates')  #static_folder='../static',

from . import views