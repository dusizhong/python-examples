# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DateTimeField,RadioField,SelectMultipleField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length


class blogForms(Form):
    title = StringField(label=u'标题', validators=[DataRequired()])
    keyword = StringField(label=u'关键字', validators=[DataRequired()])
    source = StringField(label=u'文章来源', validators=[DataRequired()])
    description = StringField(label=u'简介', validators=[DataRequired()])
    lasttime= DateTimeField(label=u'时间', validators=[DataRequired()])
    status= BooleanField(label=u'审核状态', validators=[DataRequired()])
    comment_status= BooleanField(label=u'评论状态', validators=[DataRequired()])
    smeta= StringField(label=u'缩略图', validators=[DataRequired()])
    hits= StringField(label=u'浏览量', validators=[DataRequired()])
    zan= StringField(label=u'点赞数', validators=[DataRequired()])
    top = RadioField(label=u'置顶', validators=[DataRequired()])
    recommend = RadioField(label=u'推荐', validators=[DataRequired()])
    slide = RadioField(label=u'幻灯片', validators=[DataRequired()])
    content= StringField(label=u'正文', validators=[DataRequired()])
    submit = SubmitField(label=u'发布')