class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        N = len(words)
        self.order = order
        
        for i in range(N-1):
            if not self.are_in_order(words[i], words[i + 1]):
                return False
        
        return True
    
    def are_in_order(self, word1, word2):
        
        n, m = len(word1), len(word2)
        
        for i in range(min(n, m)):
            idx1 = self.order.index(word1[i])
            idx2 = self.order.index(word2[i])
            
            if idx1 < idx2:
                return True
            elif idx2 < idx1:
                return False
        return True if n <= m else False
            