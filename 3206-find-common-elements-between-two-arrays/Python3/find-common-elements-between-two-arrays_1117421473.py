class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        return [sum(cnt1[k] for k, v in cnt2.items()), sum(cnt2[k] for k, v in cnt1.items())]