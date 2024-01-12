class BIT:
    def __init__(self, n): 
        self.sums = [0] * (n + 1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i] 
            i -= i & (-i)
        return res

class LUPrefix:

    def __init__(self, n: int):
        self.bit = BIT(n)
        self.n = n

    def upload(self, video: int) -> None:
        self.bit.update(video, 1)

    def longest(self) -> int:
        # upper bound search
        lower, upper = 0, self.n 
        while lower <= upper:
            mid = (lower + upper)//2
            cand = self.bit.query(mid)
            if cand < mid:
                upper = mid - 1
            else:
                lower = mid + 1
        return upper



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()