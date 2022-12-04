import functools

class InvalidFilter(Exception):
    print('The country param is invalid')

class InvalidDataStructure(Exception):
    print('The structure of your data is unsupported by the refinement process')

class InvalidErrorTypeInDecorator(Exception):
    def __init__():

exceptions = {
        'InvalidFilter': InvalidFilter,
        'InvalidDataStructure': InvalidDataStructure,
        'InvalidErrorTypeInDecorator': InvalidErrorTypeInDecorator
    }

def throws_error(error_type: str):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print('inside wrapper')
            try:
                return function(*args, **kwargs)
            except:
                raise exceptions[error_type]
        return wrapper
    return decorator