from flask import jsonify, abort, request, url_for
from flask.ext.restful import Api, Resource,reqparse,fields, marshal
from .models import tasks
from . import api,apiRest,auth
from .. import app,db
from ..models import User



class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

apiRest.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

class TaskListAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True,
            help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks': tasks}

    def post(self):
        if not request.json or not 'title' in request.json:
            abort(400)
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        return {'task': task}, 201

apiRest.add_resource(TaskListAPI, '/todo/api/v2.0/tasks', endpoint = 'tasks')

class TaskAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        return {'tasks':  tasks[id-1]}

    def put(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
            task = task[0]
            args = self.reqparse.parse_args()
            for k, v in args.iteritems():
                if v != None:
                    task[k] = v
        #return { 'task': make_public_task(task) }, 201
        #marshal 蒙版
        return { 'task': marshal(task, task_fields) }

    def delete(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return {'result': True}


apiRest.add_resource(TaskAPI, '/todo/api/v2.0/tasks/<int:id>', endpoint = 'task')

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@api.route('/api/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True