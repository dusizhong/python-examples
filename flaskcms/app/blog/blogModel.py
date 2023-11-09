from .. import db



class Blog(db.Model):
    __tablename__ = 'fc_blog'
    id = db.Column(db.Integer,primary_key=True,index = True,unique = True)
    cid = db.Column(db.Integer, db.ForeignKey('fc_category_blog.cid'))
    title = db.Column(db.String(120),index = True,nullable = False)
    keyword = db.Column(db.String(255))
    source = db.Column(db.String(255))
    description = db.Column(db.String(255))
    smeta = db.Column(db.String(255))
    hits = db.Column(db.Integer,default=0)
    zan = db.Column(db.Integer,default=0)
    addtime = db.Column(db.DateTime)
    lasttime = db.Column(db.DateTime,index = True)
    status = db.Column(db.SmallInteger,index = True,default=1)
    comment_status = db.Column(db.SmallInteger,default=1)
    top = db.Column(db.SmallInteger,default=0)
    recommend = db.Column(db.SmallInteger,default=0)
    slide = db.Column(db.SmallInteger,default=0)
    content = db.Column(db.Text,nullable = False)


class Category(db.Model):
    __tablename__ = 'fc_category'
    cid = db.Column(db.Integer,primary_key=True,index = True,unique = True)
    title = db.Column(db.String(64),index = True,nullable = True)
    seo_keywords = db.Column(db.String(64))
    seo_description = db.Column(db.String(255))
    parent_id = db.Column(db.SmallInteger,default=0,index = True)
    listorder = db.Column(db.SmallInteger,default=0)
    category_info = db.relationship('CategoryBlog',backref='Category',lazy='dynamic')


class CategoryBlog(db.Model):
    __tablename__ = 'fc_category_blog'
    id = db.Column(db.Integer,primary_key=True,index = True)
    cid = db.Column(db.Integer,index = True,nullable = True)
    title = db.Column(db.String(64), db.ForeignKey('fc_category.title'))
    bid = db.Column(db.Integer,index = True,nullable = True)
    listorder = db.Column(db.SmallInteger,default=0)
    blog_info = db.relationship('Blog',backref='fc_category_blog',lazy='dynamic')