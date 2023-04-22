class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 : return 0
        sign = 1
        ans = 0
        if s[0] in "-": sign = -1
        if s[0] in "+-": s = s[1:]
        
        for item in s:
            if not item.isdigit():
                break
            ans = ans * 10 + int(item)
        
        return max(-2**31, min(2**31 - 1, sign * ans))