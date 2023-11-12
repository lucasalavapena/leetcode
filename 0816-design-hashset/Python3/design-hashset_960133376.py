class MyHashSet:

    def __init__(self):
        self.entry = [False] * 10_000_000

    def add(self, key: int) -> None:
        self.entry[key] = True

    def remove(self, key: int) -> None:
        self.entry[key] = False

    def contains(self, key: int) -> bool:
        return self.entry[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)