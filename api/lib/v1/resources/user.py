from flask import request
from ..extraResource import ExtraResource


class LogIn(ExtraResource):
    def post(self):
        return str(request.get_json())


class SignUp(ExtraResource):
    def post(self):
        return str(request.get_json())
