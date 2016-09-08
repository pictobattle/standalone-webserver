from flask_restful import abort
from ..extraResource import ExtraResource
from flask import request


class Profile(ExtraResource):
    def get(self, profileID=None):
        if profileID is None:
            abort(405)
        else:
            return {'action': 'get', 'profile_ID': profileID}

    def post(self):
        return str(request.get_json())


class ProfileTransfer(ExtraResource):
    def post(self):
        return "Transfer a profile..."
