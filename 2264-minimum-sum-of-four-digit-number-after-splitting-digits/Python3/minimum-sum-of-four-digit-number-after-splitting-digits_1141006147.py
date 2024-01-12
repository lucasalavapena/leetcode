class Solution:
    def minimumSum(self, num: int) -> int:
        nstr = sorted(str(num))
        return int(nstr[0] + nstr[2]) + int(nstr[1] + nstr[3])