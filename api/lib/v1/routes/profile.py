from flask_restful import Resource
#from flask import request


class ProfileTest(Resource):
    def get(self, test):
        return {'hello': 'world'}

'''    def post():
        return str(request.get_json())'''


class ProfileTransfer(Resource):
    def post(self, profileID):
        return "Transfer a profile..."
