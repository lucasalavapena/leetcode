class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        val = self.d[key]
        # re-insert to update list...
        self.d.pop(key)
        self.d[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            self.d[key] = value
        else:
            self.d.pop(key)
            self.d[key] = value
        if len(self.d) <= self.capacity:
            return
        first_key = self.d.keys().__iter__().__next__()
        self.d.pop(first_key)