class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        max_path = min(1, rows)
  
        @cache
        def dfs(i, j, path):
            best_path = path
            
            tmp = matrix[i][j]
            matrix[i][j] = -1
            for (x, y) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                candidate_x = i + x
                candidate_y = j + y
                if 0 <= candidate_x < rows and 0 <= candidate_y < cols and matrix[candidate_x][candidate_y] != -1 and tmp < matrix[candidate_x][candidate_y]:
                    best_path = max(dfs(candidate_x, candidate_y, path + 1), best_path)
            matrix[i][j] = tmp
            
            return best_path
        
        
        for r in range(rows):
            for c in range(cols):
                max_path = max(dfs(r, c, 1), max_path)
                # print(r, c, max_path)
        
        return max_path