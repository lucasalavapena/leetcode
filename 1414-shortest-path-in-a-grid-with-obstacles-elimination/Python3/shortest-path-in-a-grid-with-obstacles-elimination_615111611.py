from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Solution:
    
    def possible_moves(self, k, loc: tuple):
        res = []
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            curr_loc = Point(loc.x + d[0], loc.y + d[1])
            if 0 <= curr_loc.x <= self.m and 0 <= curr_loc.y <= self.n:
                if self.grid[curr_loc.x][curr_loc.y] == 0:
                    res.append((k, curr_loc))
                else:
                    if k > 0:
                        res.append((k-1, curr_loc))
        return res
        
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.m = len(grid)-1
        self.n = len(grid[0])-1
        self.grid = grid

        
        q = deque([(k, Point(0, 0), 0)])
        visited = {(0, 0): 0}
        
        while q:
            curr_k, curr_loc, move_count = q.popleft()
            
            if curr_loc.x == self.m  and curr_loc.y == self.n:
                return move_count
            
            for state in self.possible_moves(curr_k, curr_loc):
                locc = (state[1].x, state[1].y)
                if k-curr_k < visited.get(locc, float("inf")):
                    visited[locc] = k-curr_k
                    q.append((*state, move_count + 1))
        
        return -1
        
