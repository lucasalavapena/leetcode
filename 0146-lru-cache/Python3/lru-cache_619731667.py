class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.info = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.info:
            return -1
        else:
            v = self.info.pop(key)  
            self.info[key] = v
        return v
            
    def put(self, key: int, value: int) -> None:
        count = len(self.info)
        if count >= self.capacity and key not in self.info:
            self.info.popitem(last=False)
            
        if key in self.info:        
            self.info.pop(key)
        self.info[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)