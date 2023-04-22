class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = ""
        
        for p in permutations(arr):
            if p[0] * 10 + p[1] <= 23 and p[2]  < 6:
                res = max(res, str(p[0])+str(p[1]) + ":" + str(p[2])+str(p[3]))
        return res