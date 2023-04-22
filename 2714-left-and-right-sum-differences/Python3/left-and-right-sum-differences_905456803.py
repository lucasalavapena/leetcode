class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(a - b) for a, b in zip(accumulate([0] + nums[:-1]), list(accumulate(nums[:0:-1]))[::-1] + [0])]