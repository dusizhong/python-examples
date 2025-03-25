from . import db
from passlib.apps import custom_app_context as pwd_context

class Role(db.Model):
    id = db.Column(db.SmallInteger,primary_key=True)
    name = db.Column(db.String(64),nullable = True)
    users = db.relationship('User',backref='role')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64),nullable = True,index = True,unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.SmallInteger, db.ForeignKey(Role.id))
    #posts = db.relationship('Post', backref = 'User', lazy = 'dynamic')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % (self.username)

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        target.role = Role.query.filter_by(name='Guests').first()

    @staticmethod
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    @staticmethod
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

db.event.listen(User.username,'set',User.on_created)

from datetime import datetime


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80))
#     body = db.Column(db.Text)
#     pub_date = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     category = db.relationship('Category',
#         backref=db.backref('posts', lazy='dynamic'))
#
#     def __init__(self, title, body, category, pub_date=None):
#         self.title = title
#         self.body = body
#         if pub_date is None:
#             pub_date = datetime.utcnow()
#         self.pub_date = pub_date
#         self.category = category
#
#     def __repr__(self):
#         return '<Post %r>' % (self.body)

# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fid = db.Column(db.Integer)
#     name = db.Column(db.String(50))
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return '<Category %r>' % self.name

#一对多
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person',
                                lazy='dynamic')
    #如果您想要一对一关系，您可以把 uselist=False 传给 relationship() 。
    #addresses = db.relationship('Address',backref=db.backref('person', lazy='joined'), lazy='dynamic')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

#多对多

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer)
    name = db.Column(db.String(50))
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer)
    name = db.Column(db.String(50))


#这里我们配置 Page.tags 加载后作为标签的列表，
# 因为我们并不期望每页出现太多的标签。
# 而每个 tag 的页面列表（ Tag.pages）是一个动态的反向引用。
#  正如上面提到的，这意味着您会得到一个可以发起 select 的查询对象。
