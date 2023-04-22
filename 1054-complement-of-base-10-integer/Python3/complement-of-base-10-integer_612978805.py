class Solution:
    def bitwiseComplement(self, n: int) -> int:
        c = 1
        while c < n: 
            c = (c << 1) + 1
        # print(n, c, bin(c))
        return n ^ c