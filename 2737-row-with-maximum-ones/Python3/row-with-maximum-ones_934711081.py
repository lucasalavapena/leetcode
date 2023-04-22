class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]
        max_row = 0
        for i, row in enumerate(mat):
            curr_row_counts = row.count(1)
            if curr_row_counts > max_row:
                res = [i, curr_row_counts]
                max_row = curr_row_counts

        return res
