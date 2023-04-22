class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return max([[i, row.count(1)] for i, row in enumerate(mat)],key=lambda x:x[1])
