class MyHashMap:

    def __init__(self):
        self.prime = 104729
        self.arr = [-1] * self.prime
        
    def put(self, key: int, value: int) -> None:
        required_key = key % self.prime
        self.arr[required_key] = value
        
    def get(self, key: int) -> int:
        required_key = key % self.prime
        
        return self.arr[required_key]

    def remove(self, key: int) -> None:
        required_key = key % self.prime
        
        self.arr[required_key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)