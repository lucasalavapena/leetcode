class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        horz = [row[:] for row in matrix] 
        vert = [row[:] for row in matrix]

        for i in range(m):
            for j in range(1, n):
                if horz[i][j]: horz[i][j] = horz[i][j-1] + 1
        for j in range(n):
            for i in range(1, m):
                if vert[i][j]: vert[i][j] = vert[i-1][j] + 1

        total = [[0] * n for i in range(m)] 
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i > 0 and j > 0: 
                        cand = min(horz[i][j], vert[i][j])
                        if cand > total[i-1][j-1] + 1:
                            cand = total[i-1][j-1] + 1
                    else:
                        cand = 1 
                    total[i][j] = cand 
                    res += cand
        return res
