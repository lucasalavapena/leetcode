class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # merge arrays
        res = nums1 + nums2
        res.sort()
        
        n = len(res)
        
        # sort
        if n % 2 == 0:
            return (res[n//2-1] + res[n//2]) / 2.0
        else:
            return res[n//2]
        
        