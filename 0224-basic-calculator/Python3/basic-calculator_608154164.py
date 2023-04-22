class Solution:
    def calculate(self, s: str) -> int:
        num, total, sign, stack = 0, 0, 1, [1]
        it = 0
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-":
                total += num * sign * stack[-1]
                sign = 1 if s[it] == "+" else -1
                num = 0
            elif s[it] == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif s[it] == ")":
                total += num * sign * stack[-1]
                num = 0
                stack.pop()
                 
            it += 1
        return total + num * sign * stack[-1]
        
        
        
        
        