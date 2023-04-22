class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        neg_diag = set()
        pos_diag = set()
        self.res = 0
        
        board = [["."] * n for _ in range(n)]
        
        
        def backtrack(r):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if c in col or r-c in neg_diag or r + c in pos_diag:
                    continue
                
                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                board[r][c] = "."
        backtrack(0)  
        return self.res