class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        def get_start_idx():
            for i in range(1, m):
                yield (m-1 - i, 0)
            for i in range(1, n-1):
                yield (0, i)
            
        for x, y in get_start_idx():
            diag_length = min(m-x, n-y)
            diag = sorted([matrix[x + i][y + i] for i in range(diag_length)])
            for i in range(diag_length):
                matrix[x + i][y + i] = diag[i]
        return matrix  