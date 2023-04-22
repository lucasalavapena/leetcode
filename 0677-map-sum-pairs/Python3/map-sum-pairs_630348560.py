class TrieNode:
    def __init__(self, val=0):
        self.children = defaultdict(TrieNode)
        self.val = val
        
        
class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        diff = val - self.map[key]
        
        for letter in key:
            curr = curr.children[letter]
            curr.val += diff
            
        self.map[key] = val
        
    def sum(self, prefix: str) -> int:
        curr = self.root
        for letter in prefix:
            curr = curr.children[letter]
        return curr.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)