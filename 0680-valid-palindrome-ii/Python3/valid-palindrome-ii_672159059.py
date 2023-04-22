class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return  False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                cand_one = s[:l] + s[l+1:]
                cand_two = s[:r] + s[r+1:]
                return is_pali(cand_one) or is_pali(cand_two)
            l += 1
            r -= 1
        return True
      
   