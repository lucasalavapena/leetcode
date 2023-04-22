class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        cntA = [0] * 7
        cntB = [0] * 7
        cntSame = [0] * 7
        for a, b in zip(tops, bottoms):
            cntA[a] += 1
            cntB[b] += 1
            if a == b: cntSame[a] += 1
        ans = n
        for v in range(1, 7):
            if cntA[v] + cntB[v] - cntSame[v] == n:
                minSwap = min(cntA[v], cntB[v]) - cntSame[v]
                ans = min(ans, minSwap)
        return -1 if ans == n else ans