class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted([n for n in nums if n % 2 == 0]) + sorted([n for n in nums if n % 2])