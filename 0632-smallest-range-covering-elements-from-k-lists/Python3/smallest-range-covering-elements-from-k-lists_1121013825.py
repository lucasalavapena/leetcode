from heapq import heappop, heappush, heapify
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)
        min_heap = [(nums[i][0], i, 0) for i in range(N)]
        heapify(min_heap)
        max_val = max(nums[i][0] for i in range(N))
        res = [min_heap[0][0], max_val]
        while min_heap:
            val, i, j = heappop(min_heap)
            res = min([val, max_val], res, key=lambda x:(x[1]-x[0], x[0]))
            if j + 1 < len(nums[i]):
                cand = nums[i][j+1]
                heappush(min_heap, (cand, i, j+1))
                max_val = max(cand, max_val)
            else: 
                break
        return res


