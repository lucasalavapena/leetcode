class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.idxs = list(range(len(w)))
        # self.total = sum(w)

    def pickIndex(self) -> int:
        return random.choices(self.idxs, weights=self.w)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()