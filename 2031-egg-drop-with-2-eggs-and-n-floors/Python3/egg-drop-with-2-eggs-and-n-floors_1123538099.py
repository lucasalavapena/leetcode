class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 1
        while n > 0:
            n -= i
            i += 1
        return i - 1