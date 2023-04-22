class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        @cache
        def dp(i, j):
            if j == -1:
                return i == -1
            
            if p[j] == "*":
                # for zero matching 
                if dp(i, j-2): return True
                
                if i >= 0 and j -1 >= 0 and p[j-1] in {s[i], "."} and dp(i - 1, j): return True
                
            if i >= 0 and p[j] in {s[i], "."} and dp(i - 1, j - 1): return True
            
            return False
        return dp(m-1, n-1)
        
        
        
        
        
        
            
        
        