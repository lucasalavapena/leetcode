from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        # print(c)
        
        for i, s_i in enumerate(s):
            if c[s_i] == 1:
                return i
                
        return -1
                
        