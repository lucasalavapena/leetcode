import heapq

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        labels_d = defaultdict(int)
        
        remaining = numWanted
        
        values_h = [[-v, i] for i, v in enumerate(values)]
        heapq.heapify(values_h)
        
        count = 0
        
        while remaining and values_h:
            val, idx = heapq.heappop(values_h)
            
            if labels_d[labels[idx]] + 1 <= useLimit:
                labels_d[labels[idx]] += 1
                count += -val
                remaining -= 1
            
        return count