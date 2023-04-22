class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        return bool(self.searchHelper(word, curr))
        
        # for i, letter in enumerate(word):
        #     if letter = ".":
        #         return self.search(word[i+1:])
        #     else:
        #         curr = curr.children.get(letter, False)
        #         if not curr:
        #             return False
        # return curr.is_word
    
    def searchHelper(self, word, node):
        for i, letter in enumerate(word):
            if letter == ".":
                return max([self.searchHelper(word[i+1:], node.children[node_i]) for node_i in node.children]) if i + 1 < len(word) and node.children else any(child.is_word for child in node.children.values())
            else:
                node = node.children.get(letter, False)
                if not node:
                    return False
        return node.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)