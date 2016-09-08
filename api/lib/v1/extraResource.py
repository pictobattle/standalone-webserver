from flask_restful import Resource


class ExtraResource(Resource):
    def __init__(self, mongoClient):
        self.mongoClient = mongoClient
