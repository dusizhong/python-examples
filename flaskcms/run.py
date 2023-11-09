
from app import app
#app = create_app()


if __name__ == '__main__':
    import os
    os.environ['DEBUG'] = 'true'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    app.debug = True
    app.run(host='localhost', port=5000)


