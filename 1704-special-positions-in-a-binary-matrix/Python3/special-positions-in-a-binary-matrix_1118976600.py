class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return (cols:=[sum(r[j] for r in mat) for j in range(len(mat[0]))]) and sum(1 for r in mat if sum(r) == 1 and cols[r.index(1)] == 1)
        