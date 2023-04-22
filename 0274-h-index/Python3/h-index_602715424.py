class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        
        citations.sort()
        end = len(citations)
        for i, c in enumerate(citations):
            paper_more_or_equal = end-i
            if h_index > paper_more_or_equal:
                return h_index
            if paper_more_or_equal >= h_index:
                h_index = min(paper_more_or_equal, c)
        
        return h_index 