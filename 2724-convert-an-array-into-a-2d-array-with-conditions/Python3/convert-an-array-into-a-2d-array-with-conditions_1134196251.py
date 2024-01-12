class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        return [[k for k, v in cnt.items() if v >=a] for a in range(1, 1+ max(cnt.values()))]