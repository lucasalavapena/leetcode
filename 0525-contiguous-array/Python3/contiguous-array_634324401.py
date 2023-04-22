class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_size = 0
        count = 0
        table = {0: 0}
        for i, n in enumerate(nums, 1):
            count += -1 if n is 0 else 1
            
            if count in table:
                max_size = max(max_size, i - table[count])
            else:
                table[count] = i
                
        return max_size