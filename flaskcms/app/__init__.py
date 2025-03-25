from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
    #获取配置文件1
app.config.from_object('config')
    #获取配置文件2
    #app.config.from_pyfile('config')

db = SQLAlchemy(app)


#登录
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view='login'



#def create_app():


    #db.init_app(app)
    #login_manager.init_app(app)


#蓝图
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .blog import blog as blog_blueprint
app.register_blueprint(blog_blueprint)

from .common import common as common_blueprint
app.register_blueprint(common_blueprint)

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)

from .api import api as api_blueprint
app.register_blueprint(api_blueprint)

from .oauth2Server import oauth2Server as oauth2Server_blueprint
app.register_blueprint(oauth2Server_blueprint)

from .oauth2Client import oauth2Client as oauth2Client_blueprint
app.register_blueprint(oauth2Client_blueprint)




from . import views, models
    #return app
