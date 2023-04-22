class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            
            # print(nums, l, nums[l], r, nums[r])
            
            if nums[l] < nums[r]:
                if nums[l] < nums[mid]:
                    r = mid
                else:
                    l = mid
                    r =- 1
            else:
                if nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid
                    l += 1
        # print(nums, l, nums[l], r, nums[r])
        if l < len(nums):
            return min(nums[l], nums[r])
        else:
            return nums[r]
        