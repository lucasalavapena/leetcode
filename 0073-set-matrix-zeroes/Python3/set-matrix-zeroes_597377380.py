class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = not all(matrix[0])
        first_col_has_zero = False
        
        for row in matrix:
            if row[0] == 0:
                first_col_has_zero = True
                break
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
                    
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        if first_row_has_zero:
            matrix[0] = [0] * n
        
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
