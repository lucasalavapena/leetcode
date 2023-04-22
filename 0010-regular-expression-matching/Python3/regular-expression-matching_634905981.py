class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        """
        
        s = "aaa"
        p =  "a*"
        
        s = "baaab"
        p =  "ba*b"
        
        
        """
        if not p:
            return not s
        if not s:
            return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
        current_char = (s[0] == p[0] or p[0] == ".")
        if len(p) > 1 and p[1] == "*":
            return (current_char and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return current_char and self.isMatch(s[1:], p[1:])
        
        