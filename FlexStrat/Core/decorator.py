from .repository import Core_repository

def core(cls):
    if not hasattr(cls, 'run'):
        raise TypeError(f"Class {cls.__name__} must implement the 'run()' method")
    repository = Core_repository()
    repository.add(cls.__name__,cls)
    return cls