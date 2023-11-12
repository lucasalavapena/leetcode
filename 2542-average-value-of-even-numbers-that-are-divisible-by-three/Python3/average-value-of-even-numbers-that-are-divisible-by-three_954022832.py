class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = [n for n in nums if n % 6 == 0]
        return sum(res)//len(res) if res else 0