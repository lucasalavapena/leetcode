import random
class Solution:
    def __init__(self, nums: List[int]):
        self.info = defaultdict(list)
        for i, n in enumerate(nums):
            self.info[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.info[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)