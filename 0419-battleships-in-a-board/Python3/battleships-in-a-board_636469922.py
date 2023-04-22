class DSU:
    def __init__(self, n):
        self.pr = list(range(n))
        self.connected_components = n
        
    def find(self, x):
        if self.pr[x] != x:
            self.pr[x] = self.find(self.pr[x])
        return self.pr[x]

    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        
        
        if x == y:
            return False
        else:
            self.connected_components -= 1
            self.pr[y] = x
            return True


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        N = list(chain(*board)).count("X")
        if N == 0: return 0
        dsu = DSU(N)
        d = {}
        
        m = len(board)
        n = len(board[0])
        
        count = 0
        for r in range(m):
            for c in range(n):
                
                if board[r][c] == "X":
                    d[(r, c)] = count
                    # top
                    if r -1 >= 0 and (r-1, c) in d and board[r-1][c] == "X":
                        idx = d[(r-1, c)]
                        dsu.union(count, idx)
                   # bottom
                    if r + 1 < m and (r+1, c) in d and board[r+1][c] == "X":
                        idx = d[(r+1, c)]
                        dsu.union(count, idx)
                # left
                    if c -1 >= 0 and (r, c-1) in d and board[r][c-1] == "X":
                        idx = d[(r, c-1)]
                        dsu.union(count, idx)
                   # bottom
                    if c + 1 < n and (r, c+1) in d and board[r][c+1] == "X":
                        idx = d[(r, c+1)]
                        dsu.union(count, idx)
                    count += 1
                    
        return dsu.connected_components
                