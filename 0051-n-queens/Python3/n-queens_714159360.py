
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        neg_diag = set()
        pos_diag = set()
        res = []
        
        board = [["."] * n for _ in range(n)]
        
        
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
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
        return res


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         self.n = n
        
#         already_tried = {}
        
#         board = [["." for j in range(n)] for i in range(n)]
#         row = [0 for i in range(n)]
#         column = [0 for i in range(n)]
#         diag = {i: 0 for i in range(-n+1, n)}
        
#     def solveNQueensHelper(self):
        
#         for i in range(self.n)
#             f
#             if self.is_legal()
        
        
#     def is_solved(self, row, column, diag):
#         return sum(row) == self.n and self.is_legal(row, column, diag)
        
#     def is_legal(self, row, column, diag) -> bool:
#         for r in row:
#             if r > 1:
#                 return False
            
#         for c in column:
#             if c > 1:
#                 return False
        
#         for d in diag:
#             if d > 1:
#                 return False
#         return True
        