class Solution:
    def halveArray(self, nums: List[int]) -> int:
        res = 0
        og_total = sum(nums)
        target_total = og_total/2
        curr_total = og_total
        
        heap = [-n for n in nums]
        heapify(heap)
        
        while curr_total > target_total:
            val = heapq.heappop(heap)
            curr_total += val/2
            heapq.heappush(heap, val/2)
            res += 1
        
        return res