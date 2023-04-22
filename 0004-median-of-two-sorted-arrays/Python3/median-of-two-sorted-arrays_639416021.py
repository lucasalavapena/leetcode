class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        
        beg, end = 0, n1
        while beg <= end:
            mid1 = (beg + end)//2
            mid2 = (n1 + n2)//2 - mid1
            
            l1 = -float("inf") if mid1 == 0 else nums1[mid1-1]
            l2 = -float("inf") if mid2 == 0 else nums2[mid2-1]
            r1 =  float("inf") if mid1 == n1 else nums1[mid1]
            r2 =  float("inf") if mid2 == n2 else nums2[mid2]
            
            if l1 > r2:
                end = mid1 - 1
            elif l2 > r1:
                beg = mid1 + 1
            else:
                return min(r1, r2) if (n1+n2)%2 else (max(l1,l2) + min(r1,r2))/2

        
        