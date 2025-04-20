from .repository import Trade_manager_repository

def run(self):
    raise NotImplementedError

def trade_manager(cls):
    if not hasattr(cls, 'run'):
        raise TypeError(f"Class {cls.__name__} must implement the 'run()' method")
    repository = Trade_manager_repository()
    repository.add(cls.__name__,cls)
    return cls