class Solution:
    
    def search(self, nums, target, lower, upper):
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] < target:
                lower = mid + 1
            elif nums[mid] > target:
                upper = mid - 1
            else:
                return mid
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bs_low, bs_high = 0, len(nums) - 1
        res = [-1, -1]
        
        bs_og = self.search(nums, target, bs_low, bs_high)

        if bs_og == -1: return res
        if res[0] == -1:
            res[0] = bs_og
        else:
            res[0] = min(bs_og, res[0]) if bs_og != -1 else res[0]
        res[1] = max(bs_og, res[1]) if bs_og != -1 else res[1]        
        # print(res)
        bs_low_upper = bs_og 
        bs_high_lower = bs_og 
        prev_bs_low_upper = -1
        prev_bs_high_lower = -1
        # print(f"{bs_og=}")
        while (bs_low_upper != prev_bs_low_upper or bs_high_lower != prev_bs_high_lower): 
            prev_bs_low_upper = bs_low_upper
            prev_bs_high_lower = bs_high_lower
            
            # print(f"{bs_low_upper=} {bs_high_lower=}")
            if bs_low_upper != -1:
                bs_low_upper = self.search(nums, target, bs_low, bs_low_upper-1)
                
                res[0] = min(bs_low_upper, res[0]) if bs_low_upper != -1 else res[0]
   
            if bs_high_lower != -1:
                bs_high_lower = self.search(nums, target, bs_high_lower+1, bs_high)

                res[1] = max(bs_high_lower, res[1]) if bs_high_lower != -1 else res[1]
            # print(f"{bs_low_upper=} {bs_high_lower=}")
            
        if bs_high - bs_high_lower == 1 and nums[bs_high_lower] == nums[bs_high]:
            res[1] = bs_high

        return res