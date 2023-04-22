class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        prev = 0
        N = len(colors)
        for i in range(1, N):
            if colors[i] != colors[prev]:
                prev = i
            else:
                if neededTime[prev] < neededTime[i]:
                    res += neededTime[prev]
                    prev = i
                else:
                    res += neededTime[i]

        return res    
            