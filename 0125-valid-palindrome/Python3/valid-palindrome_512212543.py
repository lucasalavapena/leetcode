class Solution:
    def isPalindrome(self, s: str) -> bool:
        merged = s.replace(" ", "")
        merged = ''.join([i.lower() for i in merged if i.isalpha() or i.isnumeric()])
        return merged == merged[::-1]
        