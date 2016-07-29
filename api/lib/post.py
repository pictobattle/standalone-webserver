from flask import request

mongoDB = None


def getMongo():
    return mongoDB


def get(postID):
    return "Get post number {0}!".format(postID)


def post():
    return str(request.get_json())


def update(postID):
    return "Update post number {0}!".format(postID)


def delete(postID):
    return "Delete post number {0}!".format(postID)
