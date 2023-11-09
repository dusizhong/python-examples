from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,PasswordField
from wtforms.validators import DataRequired,Email,Regexp,Length,EqualTo

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    beizhu = StringField('beizhu', validators=[DataRequired()])

class doLoginForm(Form):
    zheng = Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,u'用户名必须有字母数/数字/下划线/.组成')
    username = StringField('username', validators=[DataRequired(),zheng])
    password = PasswordField(label=u'密码', validators=[DataRequired()])
    password2 = PasswordField(label=u'密码确认', validators=[DataRequired(),EqualTo('password2',message=u'密码不一致')])
    email = StringField(label=u'邮箱', validators=[DataRequired(),Length(1,64),Email()])