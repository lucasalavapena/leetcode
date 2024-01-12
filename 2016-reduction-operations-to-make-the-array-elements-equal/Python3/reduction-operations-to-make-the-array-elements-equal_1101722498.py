class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        return sum(len(list(g)) * i for i, (_, g) in enumerate(groupby(sorted(nums))))

