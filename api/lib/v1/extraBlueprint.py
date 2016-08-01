from flask import Blueprint


class ExtraBlueprint(Blueprint):
    mongoClient = None

    def __init__(self, *args, **kwargs):
        super(ExtraBlueprint, self).__init__(*args, **kwargs)

    def register(self, app, options, first_registration=False):
        ''' This executes on Flask.register_blueprint() '''
        self.mongoClient = app.config.get('MONGO_CLIENTv1')

        super(ExtraBlueprint, self).register(app, options, first_registration)
