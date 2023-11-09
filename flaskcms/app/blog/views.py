from flask import render_template, request, flash, redirect, url_for
from . import blog
from . import blogForms
from .. import db
from . import blogModel

@blog.route('/addblog', methods=['GET', 'POST'])
def addblog():
    #return "4334"

    #form = blogForms.blogForms()

    #if form.validate_on_submit():
        # user = User(email=form.email.data,
        #             name=form.username.data,
        #             password=form.password.data)
        #
        # db.session.add(user)
        # db.session.commit()
        # return redirect(url_for('auth.login'))
        #return "123"

    return render_template('addblog.html')