class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return True
        
        if nums[1] > nums[0]:
            for i in range(2, N):
                if nums[i] < nums[i-1]:
                    return False
            return True
        elif nums[1] == nums[0]:
            is_increase = None
            for i in range(2, N):
                if nums[i] < nums[i-1]:
                    if is_increase is not None and is_increase:
                        return False
                    is_increase = False
                elif nums[i] == nums[i-1]:
                    pass
                else:
                    if is_increase is not None and not is_increase:
                        return False
                    is_increase = True
            return True
        else:
            for i in range(2, N):
                if nums[i] > nums[i-1]:
                    return False
            return True