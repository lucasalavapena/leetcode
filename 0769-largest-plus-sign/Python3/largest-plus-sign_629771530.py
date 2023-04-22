class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        grid = {tuple([x+1, y+1]) for x, y in mines}
        dp = [[[0] * 4 for _ in range(N+2)] for _ in range(N+2)]
        
        for dx, dy, dr in [(-1,0,0),(1,0,1),(0,-1,2),(0,1,3)]:
            for x in range(1,N+1)[::(-dx>=0)*2-1]:
                for y in range(1,N+1)[::(-dy>=0)*2-1]:
                    if (y, x) not in grid:
                        dp[y][x][dr] = dp[y+dy][x+dx][dr] + 1
                                                
        return max(min(q) for p in dp for q in p) 
        