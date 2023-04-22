from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a = Counter(s)
        b = Counter(t)
                
        for ele in a:
            if a[ele] != b[ele]:
                return False
            
        return True
        
        