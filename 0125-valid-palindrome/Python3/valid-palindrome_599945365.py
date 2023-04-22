class Solution:
    def isPalindrome(self, s: str) -> bool:
        transformed = ''.join([i for i in s.lower().strip() if i.isalpha() or i.isnumeric()])
        i, j = 0, len(transformed)-1
        
        while i <= j:
            if transformed[i] != transformed[j]:
                return False
            i += 1
            j -= 1
        return True