class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [-1] * n
        
        n_d = {i: val for i, val in enumerate(nums1)}
        
        m_d = {}
        stack = []
        for j, n2 in enumerate(nums2):
            
            while stack and stack[-1] < n2:
                m_d[stack[-1]] = n2
                stack.pop()
                
            stack.append(n2)
            
            
        # for k, v in n_d.items():
        #     res[k] = m_d.get(v, -1)
        #           [m_d.get(v, -1) for k, v in n_d.items()]  
        return [m_d.get(v, -1) for k, v in n_d.items()]  