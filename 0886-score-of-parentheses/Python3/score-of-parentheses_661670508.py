class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for si in s:
            if si == "(":
                stack.append(0)
            else:
                n = stack.pop()
                stack[-1] += 1 if n == 0 else 2 * n
        return stack[0]
            
        
        
        