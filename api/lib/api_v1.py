from pymongo import MongoClient

# Blueprint imports
from v1.post import post
from v1.profile import profile
from v1.user import user

# Static variables
API_VERSION = 'v1'
PREFIX = '/' + API_VERSION
MONGO_CLIENT = MongoClient()


def setUpEB(eBlueprint):
    ''' Setup ExtraBlueprints '''
    eBlueprint.setMongoClient(MONGO_CLIENT)


class APIv1(object):
    def __init__(self, app):
        setUpEB(post)
        app.register_blueprint(post, url_prefix=PREFIX + '/post')

        setUpEB(profile)
        app.register_blueprint(profile, url_prefix=PREFIX + '/profile')

        setUpEB(user)
        app.register_blueprint(user, url_prefix=PREFIX + '/user')

        @app.route(PREFIX + '/')
        def hello():
            return "API v1 says Hello World!"
