class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            # even 
            res += self.countSubstringsHelper(s, i, i + 1)
            # odd
            res += self.countSubstringsHelper(s, i, i)
        
        return res
    
    def countSubstringsHelper(self, s, l, r):
        count = 0

        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count