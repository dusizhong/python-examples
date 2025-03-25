
from flask import render_template, request, flash, redirect, url_for
from . import admin
from .. import db

@admin.route('/admin', methods=['GET', 'POST'])
def adminIndex():
    return render_template('adminIndex.html')