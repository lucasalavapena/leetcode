class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1, n + 1):
            res += bin(i)[2:]
        # print(res)
        res = f"0b{res}"
        return int(res, 2) % (10**9 + 7) 
