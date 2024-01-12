class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        right_most_idx = {n: i for i, n in enumerate(nums)}
        PRIME = 1_000_000_007
        groups = 0
        current_largest_end = 0
        for i, n in enumerate(nums):
            current_largest_end = max(current_largest_end, right_most_idx[n])
            groups += i == current_largest_end
        return pow(2, groups-1,PRIME)