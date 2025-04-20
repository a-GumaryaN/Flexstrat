def repository_decorator(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            instances[cls].repository = {}
            instances[cls].add = lambda key, value: instances[cls].repository.__setitem__(key, value)
            instances[cls].get = lambda key: instances[cls].repository.get(key)
            instances[cls].remove = lambda key: instances[cls].repository.pop(key, None)
            instances[cls].get_all = lambda: instances[cls].repository.copy()
        return instances[cls]
    
    return get_instance