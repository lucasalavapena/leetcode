class Solution:
    def findComplement(self, num: int) -> int:
        logged = math.log2(num)
        full = 1<<math.ceil(logged)

        if logged % 1 == 0: return full-1
        not_num = ~num
        return not_num + full
        