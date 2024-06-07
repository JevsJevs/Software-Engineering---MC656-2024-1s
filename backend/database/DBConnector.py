#This is not thread safe, as this will not be paralleled processed, for now, this is fine
class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class DBConnect(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

    
