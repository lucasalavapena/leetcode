"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # binary search with two x, y
#         lx, rx = 1, 1000
#         ly, ry = 1, 1000
        res = []
        max_y = 1001
        for x in range(1, 1001):
            for y in range(1, max_y):
                val = customfunction.f(x, y)
    
                if val > z:
                    max_y = y
                    break
                
                if val == z:
                    res.append([x, y])
                
        return res