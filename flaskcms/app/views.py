from flask import render_template, flash, redirect, url_for, make_response, abort, jsonify, request
from . import app
from .forms import LoginForm,doLoginForm
from .models import User

import json


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

# index view function suppressed for brevity

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))

        newuser = User(nickname=form.beizhu.data,email=form.openid.data)
        db.session.add(newuser)
        db.session.submit(newuser)
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@app.route('/post', methods = ['GET', 'POST'])
def post():
    flash(u'登录成功')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']




        return render_template('dopost.html',username = username,password = password)
    else:
        form = doLoginForm()
        list = [{'a':"A",'b':(2,4),'c':3.0}]
        list2 = ['Michael', 'Bob', 'Tracy']
        data_string = json.dumps(list2)
        decoded = json.loads(data_string)
        dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
        data_string2 = json.dumps(dic)
        return  data_string2

        return render_template('post.html',form = form)





@app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)