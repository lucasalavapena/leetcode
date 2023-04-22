class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        res = 0
        N = len(citations)
        
        for i, c in enumerate(citations):
            if N - i >= c:
                res = max(res, c)
            elif N - i >= res and c >= res:
                res = max(res, N - i)

        return res