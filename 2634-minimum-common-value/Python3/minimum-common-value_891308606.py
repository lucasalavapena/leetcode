class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = set(nums1) & set(nums2)
        return min(res) if res else -1