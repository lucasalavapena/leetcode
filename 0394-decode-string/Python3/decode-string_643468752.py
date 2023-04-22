class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        
        stack = []
        
        for si in s:
            if si != "]":
                stack.append(si)
            else:
                intermediate = ""
                while stack[-1] != "[":
                    intermediate += stack.pop()
                intermediate = intermediate[::-1]
                stack.pop()
                multiplier = ""
                while stack and "0" <= stack[-1] <=  "9":
                    multiplier += stack.pop()
                multiplier = int(multiplier[::-1])
                
                if not stack:
                    res += intermediate * multiplier
                else:
                    stack.extend(intermediate * multiplier)
        return res if not stack else res + "".join(stack)