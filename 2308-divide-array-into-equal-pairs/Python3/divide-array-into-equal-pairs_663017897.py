class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        
        for k, v in cnt.items():
            if v % 2:
                return False
        return True