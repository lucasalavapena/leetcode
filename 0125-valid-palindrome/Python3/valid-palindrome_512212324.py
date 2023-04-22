class Solution:
    def isPalindrome(self, s: str) -> bool:
        merged = s.lower().replace(" ", "")
        merged = ''.join([i for i in merged if i.isalpha() or i.isnumeric()])
        return merged == merged[::-1]
        