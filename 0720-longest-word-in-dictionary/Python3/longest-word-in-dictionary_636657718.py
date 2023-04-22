class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children[letter]
        curr.is_word = True
    
    def find_longest_word(self):
        self.words = []
        self.max_len = 0
        curr = self.root
        self.find_longest_word_helper(self.root, "")
        
        # handle ties
        self.words.sort()
        
        return self.words[0]
        
    def find_longest_word_helper(self, curr, word):
        
        current_length = len(word)
        
        if self.max_len == current_length:
            self.words.append(word)
        elif self.max_len < current_length:
            self.max_len = current_length
            self.words = [word]
            
        
        for letter in curr.children:
            if curr.children[letter].is_word:
                self.find_longest_word_helper(curr.children[letter], word + letter)
            
                
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid = set([""])
        for word in sorted(words, key=len):
            if word[:-1] in valid:
                valid.add(word)
        return max(sorted(valid), key=len)
        