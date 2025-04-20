from .repository import Visualizer_repository

def run(self):
    raise NotImplementedError

def visualizer(cls):
    if not hasattr(cls, 'run'):
        raise TypeError(f"Class {cls.__name__} must implement the 'run()' method")
    repository = Visualizer_repository()
    repository.add(cls.__name__,cls)
    return cls