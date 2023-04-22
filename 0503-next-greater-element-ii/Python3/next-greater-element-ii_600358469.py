class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums*2)
        stack = []
        for j, n in enumerate(nums*2):
            while stack and stack[-1][1] < n:
                res[stack[-1][0]] = n
                stack.pop()
                
            stack.append([j, n])
        return res[:len(nums)]
            
        