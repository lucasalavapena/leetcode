class Solution:
    def minTimeToType(self, word: str) -> int:
        new_words = [ord(w) - 97 for w in word] 
        loc = 0
        cost = 0
        for w in new_words:
            cost += min( abs(w-loc), abs(w - (loc + 26)), abs(w + 26 - loc) ) + 1
            loc = w            
        return cost
        
        