from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for r in ransomNote:
            if r not in c: return False
            c[r] -= 1
            if c[r] < 0:
                return False
            
        return True