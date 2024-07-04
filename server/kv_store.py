
class KeyValueStore:
    def __init__(self):
        self.store = {}

    def create(self, key, value):
        if key in self.store:
            return False
        self.store[key] = value
        return True

    def read(self, key):
        return self.store.get(key, None)

    def update(self, key, value):
        if key not in self.store:
            return False
        self.store[key] = value
        return True

    def delete(self, key):
        if key not in self.store:
            return False
        del self.store[key]
        return True
