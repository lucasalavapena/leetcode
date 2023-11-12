class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        total = 0
        for i in range(N):
            secondary_idx = N - 1 - i
            primary = mat[i][i]
            secondary = mat[i][secondary_idx] if i != secondary_idx else 0
            total += primary + secondary
        return total