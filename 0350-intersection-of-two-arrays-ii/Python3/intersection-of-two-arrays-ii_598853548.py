from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        
        if len(c1) < len(c2):
            smaller_c = c1
            larger_c = c2
        else:
            smaller_c = c2
            larger_c = c1
        
        for i in smaller_c:
            no = min(smaller_c[i], larger_c.get(i, 0))
            res += [i] * no
            
        return res
        