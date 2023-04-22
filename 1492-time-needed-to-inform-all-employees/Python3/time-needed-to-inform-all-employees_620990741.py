from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n < 2:
            return 0
        
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        
        return max(map(dfs, range(n)))