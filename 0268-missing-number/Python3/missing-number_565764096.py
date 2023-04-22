class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(range(len(nums)+1))
        res = numbers.symmetric_difference(set(nums))
        # for num in nums:
        #     # print(num, numbers)
        #     numbers.remove(num)
            # print(num, numbers)
        # print(numbers)
        return [s for s in res][0]
        # return numbers[0]