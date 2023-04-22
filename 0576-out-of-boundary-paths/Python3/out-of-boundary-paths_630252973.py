class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        @cache
        def dfs(x, y, move_count):
            total = 0
            if 0 <= x < m and 0 <= y < n:
                if move_count < maxMove:
                    for dx, dy in moves:
                        total += dfs(x + dx, y + dy, move_count + 1)
                else:
                    return 0
            else:
                # print(x, y)
                return 1
            
            return total % (10**9 + 7)
            
            
            # if x, y
            # total = 0
            # if 0 <= x + dx < m and 0 <= y + dy <= n:
            # ways = 0
            # for dx, dy in move:
            #     if 0 <= x + dx < m and 0 <= y + dy <= n:  
            
        # print("---"* 4)
        return dfs(startRow, startColumn, 0)