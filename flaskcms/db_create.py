
#from migrate.versioning import api
#from config import SQLALCHEMY_DATABASE_URI
#from config import SQLALCHEMY_MIGRATE_REPO
from flask_script import Manager

#数据库迁移
from flask_migrate import Migrate,upgrade,MigrateCommand

from app import app,db
#from app.models import User
from app.blog.blogModel import Blog,Category,CategoryBlog

import os.path



manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def creat():
    db.create_all()

@manager.command
def save():
    user = User('arick','arick@qq.com','1')
    db.session.add(user)
    db.session.commit()

@manager.command
def save2():
    user1 = User('arick','arick@qq.com','1')
    user2 = User('jenny','jenny@163.com','1')
    db.session.add_all([user1,user2])
    db.session.commit()

@manager.command
def query_all():
    users = User.query.all()
    for u in users:
        print(u)


@manager.command
def query_deluser():
    #删除
    me = User('jim', 'jim@qq.com','0')
    db.session.delete(me)
    db.session.commit()

@manager.command
def query_selectuser():
    #查询
    peter = User.query.filter_by(nickname='tom').first()
    print(peter.email)

@manager.command
def query_selectbyid():
    #查询
    peter = User.query.filter(id>3).first_or_404()
    print(peter.email)

@manager.command
def query_se2user():
    #复杂查询
    re = User.query.filter(User.email.endswith('@qq.com')).all()
    print(re)

@manager.command
def query_orderuser():
    #排序
    re = User.query.order_by(User.nickname).all()
    print(re)

@manager.command
def query_limituser():
    #限制数量
    re = User.query.limit(1).all()
    print(re)

@manager.command
def query_getuser():
    #主键查询用户
    re = User.query.get(2)
    print(re)

@manager.command
def query_showme():
    #主键查询用户
    re = User.query.order_by(User.nickname).limit(3).all()
    print(re)

#在视图中查询
# @app.route('/user/<username>')
# def show_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('show_user.html', user=user)

#迁移工具使用
#创建迁移目录
#python db_creat.py db init
#备份数据结构
#python db_creat.py db migrate -m 'initlal migration'
#还原数据结构
#python db_creat.py db upgrade

#还原数据结构2 数据
@manager.command
def deploy():
    from app.models import Role
    upgrade()
    Role.seed()



if __name__ == '__main__':
    manager.run()