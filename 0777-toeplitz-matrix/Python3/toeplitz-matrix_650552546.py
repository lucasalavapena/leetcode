class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        longest_diag = min(m, n)
        def get_start_idx():
            for i in range(m):
                yield (m-1 - i, 0)
            for i in range(1, n):
                yield (0, i)
            
        for x, y in get_start_idx():
            val = matrix[x][y]
            for i in range(1, longest_diag):
                if x + i >= m or y + i >= n:
                    break
                if matrix[x + i][y + i] != val:
                    return False
        return True 