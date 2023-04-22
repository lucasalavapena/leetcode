class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        no_rows = len(matrix)
        no_cols = len(matrix[0])
        
        cols = no_cols * [0]
        rows = no_rows * [0]
        
        for r in range(no_rows):
            for c in range(no_cols):
                if not matrix[r][c]:
                    rows[r] = 1
                    cols[c] = 1
        
        for i, c in enumerate(cols):
            if c:
                for r in range(no_rows):
                    matrix[r][i] = 0
                
        for i, r in enumerate(rows):
            if r:
                matrix[i] = [0] * no_cols
        
                    