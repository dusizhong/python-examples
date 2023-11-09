from flask import render_template, request, flash, redirect, url_for

from . import auth
from . import forms
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    cu = url_for('auth.register')
    return render_template('register.html',
                           title=u'注册',
                           cu = cu)

@auth.route('/reg', methods=['GET', 'POST'])
def reg():
    cu = url_for('.register')
    u = url_for('static', filename='style.css')
    return render_template('reg.html',
                           title=u'注册',
                           cu = cu,
                           u=u)


