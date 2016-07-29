import types


def appRoute(function, app, prefix='', methods=None):
    '''Add an app.route based on the name of the function'''
    kwargs = {}
    if methods is not None:
        kwargs['methods'] = methods

    app.route('/' + prefix + function.__name__ + '/', **kwargs)(function)


def appRouteAll(functions, *args, **kwargs):
    '''Add an app.route based on the name of the functions in the list'''
    for func in functions:
        appRoute(func, *args, **kwargs)


def getAllFunctions(module):
    return [module.__dict__.get(a) for a in dir(module)
            if isinstance(module.__dict__.get(a), types.FunctionType)]
