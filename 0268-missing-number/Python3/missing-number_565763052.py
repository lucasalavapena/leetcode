class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(range(len(nums)+1))
        for num in nums:
            # print(num, numbers)
            numbers.remove(num)
            # print(num, numbers)
        # print(numbers)
        return [s for s in numbers][0]
        # return numbers[0]