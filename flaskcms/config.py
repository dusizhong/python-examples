import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#数据库相关
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://personzyx:Person2016com@112.126.69.157:3306/test'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


#oauth2 server 配置
#OAUTH2_PROVIDER_ERROR_URI = 	        #当有一个错误的错误页面，默认值是'/ OAuth的/错误“。
#OAUTH2_PROVIDER_ERROR_ENDPOINT	    #您还可以配置与端点名称错误页面URI。
#OAUTH2_PROVIDER_TOKEN_EXPIRES_IN	#默认承载标记过期时间，默认为3600。
extend_existing=True