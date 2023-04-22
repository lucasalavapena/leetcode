class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        no_rows = len(matrix)
        no_columns = len(matrix[0])
        row = [0] * no_rows
        columns = [0] * no_columns
        
        for i in range(no_rows):
            for j in range(no_columns):
                if matrix[i][j] == 0:
                    # print(i, j, row, columns)
                    if not row[i]:
                        row[i] = 1
                        
                    if not columns[j]: 
                        columns[j] = 1
                        
                        
                        
        for i in range(no_rows):
            if row[i]:
                matrix[i] = [0] * no_columns
                
        for j in range(no_columns):
            if columns[j]:
                for i in range(no_rows):
                    matrix[i][j] = 0

                