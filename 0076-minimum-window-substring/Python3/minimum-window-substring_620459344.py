from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        required, remaining = Counter(t), len(t)
        i = start = end = 0
        
        for j, c in enumerate(s, 1):
            if required[c] > 0:
                remaining -= 1 
            required[c] -= 1
            
            if remaining == 0:
                while i < j and required[s[i]] < 0:
                    required[s[i]] += 1
                    i += 1
                remaining += 1
                if end == 0 or j-i < end-start:
                    start, end = i, j
                required[s[i]] += 1
                i += 1
                
        return s[start:end]
        
        