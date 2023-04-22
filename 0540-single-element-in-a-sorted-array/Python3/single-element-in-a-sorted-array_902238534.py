class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            if mid + 1 < N and nums[mid] == nums[mid + 1]:
                if (mid + 1) % 2:
                    lower = mid + 2
                else:
                    upper = mid - 1
            elif 0 <= mid - 1 and nums[mid - 1] == nums[mid]:
                if mid % 2:
                    lower = mid + 1
                else:
                    upper = mid - 1
            else:
                return nums[mid]


        return -1
