class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def get_simpified(digit):
            return [int(e) for e in str(digit)]
        
        total_res = []
        for item in nums:
            total_res += get_simpified(item)
        return total_res