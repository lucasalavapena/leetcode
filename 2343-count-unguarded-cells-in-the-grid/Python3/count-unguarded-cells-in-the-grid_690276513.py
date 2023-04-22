class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for j in range(n)] for i in range(m)]
        
        for w_x, w_y in walls:
            grid[w_x][w_y] = -1
            
        visited = set()
        
        for guard_id, (g_x, g_y) in enumerate(guards):
            # top
            for i in range(g_x, m):
                
                if grid[i][g_y] != -1 and (i, g_y, "top") not in visited and (i, g_y, "down") not in visited:
                    grid[i][g_y] = 1
                    visited.add((i, g_y, "top"))
                else:
                    break
                    
            # down
            for i in range(g_x - 1, -1, -1):

                if grid[i][g_y] != -1 and (i, g_y, "top") not in visited and (i, g_y, "down") not in visited:
                    grid[i][g_y] = 1
                    visited.add((i, g_y, "down"))
                else:
                    break
            
            # right
            for i in range(g_y, n):
                if grid[g_x][i] != -1 and (g_x, i, "left") not in visited and (g_x, i, "right") not in visited:
                    grid[g_x][i] = 1
                    visited.add((g_x, i, "right"))
                else:
                    break
            
            # left
            for i in range(g_y - 1, -1, -1):
                if grid[g_x][i] != -1 and (g_x, i, "left") not in visited and (g_x, i, "right") not in visited:
                    grid[g_x][i] = 1
                    visited.add((g_x, i, "left"))
                else:
                    break
        return sum([grid[i][j] == 0 for j in range(n) for i in range(m)])