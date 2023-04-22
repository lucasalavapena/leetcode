class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        stack = []
        for i in range(N):
            while k > 0 and stack:
                if stack[-1] > num[i]:
                    stack.pop()
                    k -= 1
                else:
                    break
                
            stack.append(num[i])
            
        while k != 0:
            stack.pop()
            k -= 1
            
        for i in range(len(stack)):
            if stack[i] != "0":
                break
                
        stack = stack[i:]  
        
        if not stack:
            return "0"
        return "".join(stack)