class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        # 1. Capture counts of smallest characters in each word, and sort 
        # the list in ascending order.
        W = sorted([w.count(min(w)) for w in words])
        
        res = []
        for q in queries:
            # 2. Perform binary search of smallest characters in each query
            # against the sorted list from step#1.
            cnt = q.count(min(q))
            idx = bisect.bisect_right(W, cnt)
            res.append(len(words) - idx)
        return res
