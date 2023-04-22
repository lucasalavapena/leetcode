class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, furthest, curr_end = 0, 0, 0             
        for i, num in enumerate(nums[:-1]): 
            furthest = max(furthest, i + num) 
            if i == curr_end:      
                steps += 1  
                curr_end = furthest
        return steps 
        