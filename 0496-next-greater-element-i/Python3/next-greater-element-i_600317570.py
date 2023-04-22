class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [-1] * n
        
        for ii, i in enumerate(nums1):
            has_passed = False
            for j in nums2:
                
                if i == j:
                    has_passed = True
                    
                if has_passed and j > i:
                    res[ii] = j
                    break
        return res