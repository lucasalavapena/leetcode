class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        tmp = ""
        for si in s:
            if si != ")":
                stack.append(si)
            else:
                while stack[-1] != "(":
                    tmp += stack.pop()
                stack.pop()
                for r in tmp:
                    stack.append(r)
                tmp = ""
                
        return "".join(stack)