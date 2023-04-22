class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        cnt = 0
        res = ""
        
        for c in s:
            stack.append(c)
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
                
            if cnt == 0:
                res += "".join(stack)[1:-1]
                stack = []
            
                
        return res
                
        
        