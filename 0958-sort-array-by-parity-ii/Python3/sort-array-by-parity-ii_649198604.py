class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [n for n in nums if n % 2]
        even = [n for n in nums if n % 2 == 0]
        
        res = []
        for a, b in zip(even, odd):
            res.append(a)
            res.append(b)
        
        return res