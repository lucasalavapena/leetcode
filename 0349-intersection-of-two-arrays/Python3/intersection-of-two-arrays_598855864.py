from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        res = []
        
        for n in nums2:
            if c[n]:
                res.append(n)
                c[n] = 0
        return res
            
        