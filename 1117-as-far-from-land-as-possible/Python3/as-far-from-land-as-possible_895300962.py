from collections import deque
from itertools import product
"""
Note that you can skip 

"""

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()

        for (i, j) in product(range(n), repeat=2):
            if grid[i][j] == 1: 
                q.append((i, j))

        if not q or len(q) == n * n: 
            return -1

        res = -1
        DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while q:
            q_len = len(q)
            res += 1
            for _ in range(q_len):
                x, y = q.popleft()
                for dx, dy in DELTAS:
                    i, j = x + dx, y + dy
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        grid[i][j] = 1
                        q.append((i, j))
        return res
