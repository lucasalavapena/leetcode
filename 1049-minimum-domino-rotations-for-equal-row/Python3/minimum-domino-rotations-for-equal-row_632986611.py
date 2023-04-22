class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        s, n = set([1,2,3,4,5,6]), len(tops)
        for i in range(n): s &= set([tops[i], bottoms[i]])
        if not s: return -1
        flips1 = sum(tops[i] == list(s)[0] for i in range(n))
        flips2 = sum(bottoms[i] == list(s)[0] for i in range(n))
        return min(n - flips1, n - flips2)  