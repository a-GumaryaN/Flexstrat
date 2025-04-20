from .repository import API_repository

def api(cls):
    if not hasattr(cls, 'run'):
        raise TypeError(f"Class {cls.__name__} has no implementation for 'run()' method")
    repository = API_repository()
    repository.add(cls.__name__,cls)
    return cls