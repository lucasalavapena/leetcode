class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        h = [[-v, k] for k, v in c.items()]

        heapq.heapify(h)
        res = [0] * k

        i = 0
        while k-i > 0:
            res[i] = heapq.heappop(h)[1]
            i += 1
            
        return res
        
        
        