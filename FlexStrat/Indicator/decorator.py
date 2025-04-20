from .repository import Indicator_repository

def run(self):
    raise NotImplementedError

def indicator(cls):
    if not hasattr(cls, 'run'):
        raise TypeError(f"Class {cls.__name__} must implement the 'run()' method")
    cls.last_index = 0
    repository = Indicator_repository()
    repository.add(cls.__name__,cls)
    return cls