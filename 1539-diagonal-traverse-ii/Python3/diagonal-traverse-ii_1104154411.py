from collections import defaultdict, deque
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = defaultdict(deque)
        n, m = len(nums), len(nums[-1])
        for i in range(n):
            for j in range(len(nums[i])):
                diag[i+j].appendleft(nums[i][j])
            
        res = []
        for key in diag:
            res.extend(diag[key])
        return res
                    
            
              