from collections import deque

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        
        @cache
        def dfs(curr_k, x, y, P):
            p = 0
            if 0 <= x < n and 0 <= y < n:
                if curr_k < k:
                    for dx, dy in moves:
                        p += dfs(curr_k + 1, x + dx, y + dy, P / len(moves))
                else:
                    p = P

            return p

        return dfs(0, row, column, 1.0)
            
        