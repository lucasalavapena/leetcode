class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        curr, res = -1001, 0
        for start, end in sorted(pairs, key=lambda x: x[1]):
            if curr < start:
                curr, res = end, res + 1
        return res