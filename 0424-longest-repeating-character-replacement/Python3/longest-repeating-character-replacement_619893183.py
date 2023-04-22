class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = maxi = 0 
        for i in range(len(s)):
            count[s[i]] += 1
            maxi = max(maxi, count[s[i]])
            
            if res - maxi < k:
                res += 1                
            else:
                count[s[i- res]] -= 1
        return res
            
        
            
        