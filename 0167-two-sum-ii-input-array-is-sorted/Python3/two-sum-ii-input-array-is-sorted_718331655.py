class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_to_idx = {n: i for i, n in enumerate(numbers)}
        for i, n in enumerate(numbers):
            required = target - n
            if required in number_to_idx:
                idx2 = number_to_idx[required]
                return [i + 1, idx2 + 1]