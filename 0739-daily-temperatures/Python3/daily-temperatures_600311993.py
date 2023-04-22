class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        
        res = [0] * n 
        
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
                
            res[i] = stack[-1]-i if stack else 0
            stack.append(i)
        return res