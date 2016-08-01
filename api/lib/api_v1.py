from pymongo import MongoClient

# Blueprint imports
from v1.post import post
from v1.profile import profile
from v1.user import user

# Static variables
API_VERSION = 'v1'
PREFIX = '/' + API_VERSION
MONGO_CONFIG = {'host': 'localhost', 'post': 27017}


class APIv1(object):
    def __init__(self, app):
        app.config['MONGO_CLIENTv1'] = MongoClient(MONGO_CONFIG['host'],
                                                   MONGO_CONFIG['port'])

        app.register_blueprint(post, url_prefix=PREFIX + '/post')

        app.register_blueprint(profile, url_prefix=PREFIX + '/profile')

        app.register_blueprint(user, url_prefix=PREFIX + '/user')

        @app.route(PREFIX + '/')
        def hello():
            return "API v1 says Hello World!"
