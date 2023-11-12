class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def is_pali(s, i, j):
            while 0 <= i and j < N:
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i + 1:j]
        
        max_str = s[0]
        
        for i in range(0, N):
            even = is_pali(s, i, i + 1)
            odd = is_pali(s, i, i)
            max_str = max(max_str, even, odd, key=len)
            
        return max_str
        
        