class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = None
        abs_closest_sum_diff = None
        N = len(nums)
        for i, n in enumerate(nums):
            l, r = i + 1, N - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r] 
                
                if closest_sum is None or abs(curr_sum-target) < abs_closest_sum_diff:
                    closest_sum = curr_sum
                    abs_closest_sum_diff = abs(curr_sum-target)
                    
                    
                if curr_sum > target:
                    r -= 1
                elif curr_sum == target:
                    return target
                else:
                    l += 1
                
                
        return closest_sum