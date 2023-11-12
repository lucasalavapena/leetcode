class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        if n < 4:
            return False
        binary = bin(n)[2:]
        even_cnt, odd_cnt = 0, 0
        for b in binary:
            if b == "0":
                even_cnt += 1
            else:
                odd_cnt += 1
                if odd_cnt > 1:
                    return False
        return False if even_cnt % 2 else True