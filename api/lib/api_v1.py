"""The APIv1 module."""
from flask_restful import Api
from flask import Blueprint
from pymongo import MongoClient

# Resource imports
from v1.resources import profile, post, user  # , user, post

# Static variables
EXTRA_RESOURCE_KWARGS = {'mongoClient': MongoClient(host='localhost',
                                                    port=27017)}

# App setup:
apiBlueprint = Blueprint('api_v1', __name__)
api = Api(apiBlueprint)


# User:
api.add_resource(user.LogIn, '/user/logIn/',
                 resource_class_kwargs=EXTRA_RESOURCE_KWARGS)
api.add_resource(user.SignUp, '/user/signUp/',
                 resource_class_kwargs=EXTRA_RESOURCE_KWARGS)


# Profile:
api.add_resource(profile.Profile, '/profile/', '/profile/<int:profileID>/',
                 resource_class_kwargs=EXTRA_RESOURCE_KWARGS)
api.add_resource(profile.ProfileTransfer, '/profile/<int:profileID>/transfer/',
                 resource_class_kwargs=EXTRA_RESOURCE_KWARGS)


# Post:
api.add_resource(post.NewPost, '/post/',
                 resource_class_kwargs=EXTRA_RESOURCE_KWARGS)
api.add_resource(post.CreatedPost, '/post/<string:postID>/',
                 '/post/<string:userID>/<int:postID>/',
                 resource_class_kwargs=EXTRA_RESOURCE_KWARGS)
