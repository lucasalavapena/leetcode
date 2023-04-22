class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        
        stack.append(pushed[i])
        i += 1
        
        while stack or i < len(pushed):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                if i < len(pushed):
                    stack.append(pushed[i])
                    i += 1 
                else:
                    break
        return False if stack else True
        
        