class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for k, v in c.items():
            if v == 1 and k - 1 not in c and k + 1 not in c:
                res.append(k)
        return res
        