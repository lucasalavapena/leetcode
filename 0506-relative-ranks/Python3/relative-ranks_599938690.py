import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        strings = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score)+2)]
        res = [""] * len(score)    
        index = {val: i for i, val in enumerate(score)}
        h = [-s for s in score]
        heapq.heapify(h)
        i = 0
        while h:
            val = heapq.heappop(h)
            res[index[-val]] = strings[i]
            i += 1
        return res