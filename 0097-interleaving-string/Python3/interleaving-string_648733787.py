class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m, n, k = len(s1), len(s2), len(s3)
        
        
        if m + n != k:
            return False
        
        # if any(v != 0 for v in (Counter(s1) + Counter(s2) - Counter(s3)).values()):
        #     return False
        
        @cache
        def dp(i, j):
            if i + j == m + n:
                return True
            
            if i + j > m + n:
                return False
            
            if i > m or j > n:
                return False
            
            # print(i, j, i + j)
            if i < m and s1[i] == s3[i + j] and dp(i + 1, j):
                return True
                
            if j < n and s2[j] == s3[i + j] and dp(i, j + 1):
                return True
        
            return False
            
        
        return dp(0, 0)
        
            
            
        