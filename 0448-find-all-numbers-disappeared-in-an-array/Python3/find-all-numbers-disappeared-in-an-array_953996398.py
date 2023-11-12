class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        seen = set(nums)
        return [s for s in range(1, N + 1) if s not in seen]
        