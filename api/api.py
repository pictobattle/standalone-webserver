from flask import Flask, request, abort
import lib.util as util

# Import method classes
import lib.user as user
import lib.post as post

# Initiate flask app
app = Flask(__name__)


@app.route('/')
def hello():
    return 'API says Hello World!'


# Post Management
app.route('/post/', methods=['POST'])(post.post)


@app.route('/post/<postID>/', methods=['GET', 'PUT', 'DELETE'])
def postRequestHandler(postID):
    if request.method == 'GET':
        return post.get(postID)
    elif request.method == 'PUT':
        return post.update(postID)
    elif request.method == 'DELETE':
        return post.delete(postID)
    else:
        abort(500)


# Module function URL routing
util.appRouteAll(util.getAllFunctions(user), app, 'user/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
