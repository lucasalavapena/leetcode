class TrieNode:
    def __init__(self):
        self.children, self.end = {}, 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, reversed_words):
        curr = self.root
        for w in reversed_words:
            # curr.children[w] = TrieNode()
            # curr = curr.children[w]
            curr = curr.children.setdefault(w, TrieNode())
        curr.end = 1
    
    
class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        self.Stream = deque()
        for word in words: self.trie.insert(word[::-1])
            
    def query(self, letter):
        self.Stream.appendleft(letter)
        curr = self.trie.root
        
        for c in self.Stream:
            if c in curr.children:
                curr = curr.children[c]
                if curr.end:
                    return True  
            else:
                break
        return False
        
        