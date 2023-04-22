class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:        
        rows, cols, res = len(matrix), len(matrix[0]), 0
        
        if list(chain(*matrix)).count("1") == rows * cols: return rows * cols
        
        dp = [[0] * (cols + 1) for r in range(rows + 1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                dp[i][j] = dp[i][j + 1] + 1 if matrix[i][j] == "1" else 0
                
        for i in range(rows):
            for j in range(cols):
                cols_pos = cols
                for k in range(i, rows):
                    if matrix[k][j] == "1":
                        cols_pos = min(cols_pos, dp[k][j])
                        res = max(res, (k-i + 1) * cols_pos)
                    else:
                        break
        return res