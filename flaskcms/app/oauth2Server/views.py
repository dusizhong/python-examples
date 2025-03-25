from flask import render_template, jsonify, session, request, redirect, url_for
#from flask_oauthlib.provider import require_login
from werkzeug.security import gen_salt
from datetime import datetime, timedelta
from . import oauth, oauth2Server
from helloFlask.app.oauth2Client.model import Client , Grant, Token
from ..models import User
from .. import db


@oauth.clientgetter
def load_client(client_id):
    return Client.query.filter_by(client_id=client_id).first()

@oauth.grantgetter
def load_grant(client_id, code):
    return Grant.query.filter_by(client_id=client_id, code=code).first()

@oauth.grantsetter
def save_grant(client_id, code, request, *args, **kwargs):
    # decide the expires time yourself
    expires = datetime.utcnow() + timedelta(seconds=100)
    grant = Grant(
        client_id=client_id,
        code=code['code'],
        redirect_uri=request.redirect_uri,
        _scopes=' '.join(request.scopes),
        user=current_user(),
        expires=expires
    )
    db.session.add(grant)
    db.session.commit()
    return grant

@oauth.tokengetter
def load_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.query.filter_by(access_token=access_token).first()
    elif refresh_token:
        return Token.query.filter_by(refresh_token=refresh_token).first()



@oauth.tokensetter
def save_token(token, request, *args, **kwargs):
    toks = Token.query.filter_by(client_id=request.client.client_id,
                                 user_id=request.user.id)
    # make sure that every client has only one token connected to a user
    for t in toks:
        db.session.delete(t)

    expires_in = token.get('expires_in')
    expires = datetime.utcnow() + timedelta(seconds=expires_in)

    tok = Token(
        access_token=token['access_token'],
        refresh_token=token['refresh_token'],
        token_type=token['token_type'],
        _scopes=token['scope'],
        expires=expires,
        client_id=request.client.client_id,
        user_id=request.user.id,
    )
    db.session.add(tok)
    db.session.commit()
    return tok

#可选
@oauth.usergetter
def get_user(username, password, *args, **kwargs):
    user = User.query.filter_by(username=username).first()
    if user.check_password(password):
        return user
    return None



def current_user():
    if 'id' in session:
        uid = session['id']
        return User.query.get(uid)
    return None

#登录界面
@oauth2Server.route('/oauth2server/home', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        session['id'] = user.id
        return redirect(url_for('oauth2Server.home'))
    user = current_user()
    return render_template('home.html', user=user)


#创件client数据
@oauth2Server.route('/oauth2server/client')
def client():
    user = current_user()
    if not user:
        return redirect('/oauth2server/home')
    item = Client(
        client_id=gen_salt(40),
        client_secret=gen_salt(50),
        _redirect_uris=' '.join([
            'http://localhost:5000/oauth2server/authorized',
            'http://127.0.0.1:5000/oauth2server/authorized'
            ]),
        _default_scopes='email',
        user_id=user.id,
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(
        client_id=item.client_id,
        client_secret=item.client_secret,
    )


# 相当于 login  授权炒作
@oauth2Server.route('/oauth2Server/authorize', methods=['GET', 'POST'])
#@require_login
@oauth.authorize_handler
def authorize(*args, **kwargs):
    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        client = Client.query.filter_by(client_id=client_id).first()
        kwargs['client'] = client
        kwargs['user'] = {'username':'arick','age':12 }
        return render_template('oauthorize.html', **kwargs,client_id=client_id)

    # confirm = request.form.get('confirm', 'no')
    # return confirm == 'yes'

# 相当于 oauth 用于产生 /刷新 token
@oauth2Server.route('/oauth2Server/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return {'version': '0.1.0'}

#撤销应用授权
@oauth2Server.route('/oauth/revoke', methods=['POST'])
@oauth.revoke_handler
def revoke_token(): pass


@oauth2Server.route('/api/me')
@oauth.require_oauth('email')
def me():
    user = request.oauth.user
    return jsonify(email=user.email, username=user.username)

@oauth2Server.route('/api/user/<username>')
@oauth.require_oauth()
def user(username):
    user = User.query.filter_by(username=username).first()
    return jsonify(email=user.email, username=user.username)



def require_login():
    pass



