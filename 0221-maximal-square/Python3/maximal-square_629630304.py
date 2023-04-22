class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        return self.dynamic_programming()
#         r, c, res = len(matrix), len(matrix[0]), 0
        
    
    
    # 1
    
    # 2 1
    # 1 1
    
    
    # x 1 0 
    # 2 2 1
    # 1 1 1
#         dp = [[0] * (c + 1) for i in range(r + 1)]
    def dynamic_programming(self):
        rows, cols, res = len(self.matrix), len(self.matrix[0]), 0
        
        dp = [[0] * (cols + 1) for col in range(rows + 1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                dp[i][j] = 1 + min(dp[i + 1][j],dp[i + 1][j + 1], dp[i][j + 1]) if self.matrix[i][j] == "1" else 0
                res = max(res, dp[i][j] * dp[i][j])
                
        return res 
        
#     def stupid(self):
#         rows, cols, res = len(matrix), len(matrix[0]), 0
        
#         for row in rows:
#             for col in cols:
#                 if matrix[row][col] == "1":
#                     res = max(res, self.expand(row, col))
#         return res
    
#     def expand(self, r, c):
#         self.matrix
        

        
        
        