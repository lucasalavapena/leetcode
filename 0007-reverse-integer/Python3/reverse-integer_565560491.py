class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        mutliplier = 1
        if x < 0:
            mutliplier = -1
            x = -x
        res = int(str(x)[::-1].lstrip("0")) * mutliplier
        if not((2 ** 31 -1) >= res >= -(2 ** 31)):
            return 0
            
        return res