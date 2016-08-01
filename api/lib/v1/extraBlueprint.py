from flask import Blueprint


class ExtraBlueprint(Blueprint):
    mongoClient = None

    def __init__(self, *args, **kwargs):
        super(ExtraBlueprint, self).__init__(*args, **kwargs)

    def setMongoClient(self, mongoClient):
        self.mongoClient = mongoClient

    def mongoClientExists(self):
        if self.mongoClient is not None:
            return True
        return False
