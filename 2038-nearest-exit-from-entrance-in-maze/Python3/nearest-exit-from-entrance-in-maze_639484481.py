class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        
        q = deque([entrance])
        move_count = -1
        maze[entrance[0]][entrance[1]] = "+"        
        while q:
            q_len = len(q)
            move_count += 1
            
            for _ in range(q_len):
                x, y = q.popleft()
                                
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xp, yp = x + dx, y + dy
                    if (
                        0 <= xp < n
                        and 0 <= yp < m
                        and maze[xp][yp] != "+"
                       ):
                        if (xp == 0 or xp == n-1 or yp == 0 or yp == m-1) and (xp != entrance[0] or yp != entrance[1]):
                            return move_count + 1
                        q.append((xp, yp))
                        maze[xp][yp] = "+"
        return -1
        