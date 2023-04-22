class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = list(range(len(nums)+1))
        for num in nums:
            # print(num, numbers)
            numbers.remove(num)
            # print(num, numbers)
        return numbers[0]