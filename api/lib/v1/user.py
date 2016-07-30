from flask import Blueprint, request

user = Blueprint('user', __name__)


# Routes:
@user.route('/logIn/', methods=['POST'])
def logIn():
    return str(request.get_json())


@user.route('/signUp/', methods=['POST'])
def signUp():
    return str(request.get_json())
