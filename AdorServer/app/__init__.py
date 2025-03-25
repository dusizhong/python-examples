from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# 获取配置文件
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable
from .product import product as product_blueprint

# Register blueprint(s)
app.register_blueprint(product_blueprint)

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()