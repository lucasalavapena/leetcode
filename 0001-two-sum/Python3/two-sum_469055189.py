from itertools import combinations
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_number_combinations = combinations(nums, 2)
        for (number_1, number_2) in two_number_combinations:
            if number_1 + number_2 == target:
                number_1_idx = nums.index(number_1)
                number_2_idx = nums.index(number_2, number_1_idx+1)
                return [number_1_idx, number_2_idx]        