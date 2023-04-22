class Solution:
    
    
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf")
        parity = 0
        local_parity = 0
        curr_product = 1
        
        prev_reset_loc = 0
        reset_loc = 0
        
        for i, n in enumerate(nums):
            if n < 0:
                parity += 1
                local_parity += 1
                
            if n < 0 and local_parity == 1:
                prev_reset_loc = reset_loc
                reset_loc = i
            
            curr_product *= n
            max_product = max(max_product, curr_product)
            
            if curr_product == 0:
                curr_product = 1
                prev_reset_loc = reset_loc
                reset_loc = i
                # print(local_parity, reset_loc)
                if local_parity % 2 == 1  and reset_loc + 1 <= len(nums):
                    to_m = list(filter(lambda num: num != 0, nums[prev_reset_loc+1:reset_loc]))
                    last_rpduct = math.prod(to_m) if len(to_m) else 0
                    # print(last_rpduct)
                    max_product = max(max_product, last_rpduct)
                
                local_parity = 0
            
            
        if local_parity % 2 == 1  and reset_loc + 1 < len(nums):
            to_m = list(filter(lambda num: num != 0, nums[reset_loc + 1:]))
            last_rpduct = math.prod(to_m) if len(to_m) else 0
            max_product = max(max_product, last_rpduct)
        return max_product