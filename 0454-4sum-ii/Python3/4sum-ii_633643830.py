class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = collections.Counter(a+b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)
  