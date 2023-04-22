class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        N = len(nums)
        
        max_average = float("-inf")
        for i, n in enumerate(nums):
            total += n
            
            if i == k-1:
                max_average = max(max_average, total/k)
                
            elif k - 1 < i:
                total -= nums[i-k]
                max_average = max(max_average, total/k)

                
        return max_average