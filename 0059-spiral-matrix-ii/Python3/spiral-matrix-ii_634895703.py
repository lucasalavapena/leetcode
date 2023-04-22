class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[1 for j in range(n)] for i in range(n)]
        
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_idx = 0
        
        visited = set()
        loc = (0, 0)
        
        # Preference R, D, L, U
        # visited
        
        for i in range(2, n * n + 1):
            visited.add(loc)
            x, y = loc
            while True:
                dx, dy = directions[dir_idx]
                if 0 <= x + dx < n and 0 <= y + dy < n and (x + dx,  y + dy) not in visited:
                    loc = (x + dx,  y + dy)
                    res[loc[0]][loc[1]] = i
                    break
                dir_idx = (dir_idx + 1) % 4
            
        return res
            
                