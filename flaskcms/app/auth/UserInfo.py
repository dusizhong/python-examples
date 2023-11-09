from flask import render_template
from flask.views import View
from ..models import User
from .. import app

class UserInfo(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserView(UserInfo):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return User.query.all()

app.add_url_rule('/myview', view_func=UserInfo.as_view('myview'))

class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name)

app.add_url_rule('/about', view_func=RenderTemplateView.as_view(
    'about_page', template_name='about.html'))