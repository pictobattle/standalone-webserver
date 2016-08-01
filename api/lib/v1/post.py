from flask import request, abort
from extraBlueprint import ExtraBlueprint

post = ExtraBlueprint('post', __name__)


# Non-route functions:
def get(**kwargs):
    return("MongoClient: {0} \n".format(str(post.mongoClient)) +
           "From user {0}, get post number {1}!"
           .format(kwargs['userID'], kwargs['postID']))


def update(**kwargs):
    return "From user {0}, update post number {1}!".format(kwargs['userID'],
                                                           kwargs['postID'])


def delete(**kwargs):
    return "From user {0}, delete post number {1}!".format(kwargs['userID'],
                                                           kwargs['postID'])


# Routes:
@post.route('/', methods=['POST'])
def create():
    return str(request.get_json())


@post.route('/<userID>/<postID>/', methods=['GET', 'PUT', 'DELETE'])
def postRequestHandler(*args, **kwargs):
    if request.method == 'GET':
        return get(*args, **kwargs)
    elif request.method == 'PUT':
        return update(*args, **kwargs)
    elif request.method == 'DELETE':
        return delete(*args, **kwargs)
    else:
        abort(500)
