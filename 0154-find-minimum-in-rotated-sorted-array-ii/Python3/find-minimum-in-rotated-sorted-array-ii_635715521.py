class Solution:
    def findMin(self, nums: List[int]) -> int:
        beg, end = 0, len(nums)-1
        
        while beg < end:
            mid = (beg + end)//2
            
            if nums[mid] > nums[end]:
                beg = mid + 1
            else:
                end = mid if nums[mid] != nums[end] else end-1
            
        return nums[beg]