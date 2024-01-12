class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        s1 = set(nums1)
        s2 = set(nums2)

        inter = len(s1 & s2)
        only_s1_take = min(len(s1) - inter, N//2)
        only_s2_take = min(len(s2) - inter, N//2)
        return min(only_s1_take + only_s2_take + inter, N)  
