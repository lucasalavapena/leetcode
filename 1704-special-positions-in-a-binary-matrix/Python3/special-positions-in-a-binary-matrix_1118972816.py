class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cols = [sum(r[j] for r in mat) for j in range(n)]
        count = 0
        for i in range(m):
            if sum(mat[i]) == 1:
                idx = mat[i].index(1)
                if cols[idx] == 1:
                    count += 1
        return count
        