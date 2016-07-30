from flask import Blueprint, request, abort

post = Blueprint('post', __name__)


# Non-route functions:
def get(postID):
    return "Get post number {0}!".format(postID)


def update(postID):
    return "Update post number {0}!".format(postID)


def delete(postID):
    return "Delete post number {0}!".format(postID)


# Routes:
@post.route('/', methods=['POST'])
def create():
    return str(request.get_json())


@post.route('/<postID>/', methods=['GET', 'PUT', 'DELETE'])
def postRequestHandler(postID):
    if request.method == 'GET':
        return get(postID)
    elif request.method == 'PUT':
        return update(postID)
    elif request.method == 'DELETE':
        return delete(postID)
    else:
        abort(500)
