class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 
        
        pivot = random.choice(nums)
        
        left = [n for n in nums if n > pivot]
        mid =  [n for n in nums if n == pivot]
        right = [n for n in nums if n < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > M + L:
            return self.findKthLargest(right, k - M -L)
        else:
            return pivot