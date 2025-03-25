from flask import  url_for, session, request, jsonify
#from flask_oauthlib.client import OAuth
from . import oauth,oauth2Client
from ..oauth2Server import oauth2Server


CLIENT_ID = '1cCep1yHM3YdnCxKeZz7JcR0jJSDnO9fYMgJHHu1'
CLIENT_SECRET = 'hBIds5tJDP6pDAlO1fKL8vt69xOCbVgluL6rlb2Tu2sCNCVLRw'


remote = oauth.remote_app(
    'remote',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'email'},
    base_url='http://127.0.0.1:5000/api/',
    request_token_url=None,
    access_token_url='http://127.0.0.1:5000/oauth2Server/token',
    authorize_url='http://127.0.0.1:5000/oauth2Server/authorize'
)


@oauth2Client.route('/oauth2Client/home')
def index():
    if 'remote_oauth' in session:
        resp = remote.get('me')
        return jsonify(resp.data)
    next_url = request.args.get('next') or request.referrer or None
    return remote.authorize(
        callback=url_for('oauth2Client.authorized', next=next_url, _external=True)
    )


@oauth2Client.route('/oauth2Client/authorized')
def authorized():
    resp = remote.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    #print resp
    session['remote_oauth'] = (resp['access_token'], '')
    return jsonify(oauth_token=resp['access_token'])


@remote.tokengetter
def get_oauth_token():
    return session.get('remote_oauth')



