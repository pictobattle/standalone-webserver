from flask import Blueprint, request

profile = Blueprint('profile', __name__)


# Non-route functions:
def getProfiles(userID):
    return "Profiles!"


# Routes:
@profile.route('/', methods=['POST'])
def create():
    return str(request.get_json())


@profile.route('/transfer/', methods=['POST'])
def transfer():
    return "Transfer a profile..."
