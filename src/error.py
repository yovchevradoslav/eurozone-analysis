class InvalidFilter(Exception):
    def __init__(self):
        self.message = 'Invalid Filter'

class InvalidDataStructure(Exception):
    def __init__(self):
        self.message = 'Invalid Data Structure'

def throws_error(exception: Exception):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except:
                raise exception
        return wrapper
    return decorator