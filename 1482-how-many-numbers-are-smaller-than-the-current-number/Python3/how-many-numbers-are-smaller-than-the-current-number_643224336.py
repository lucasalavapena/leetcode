class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        N  = len(nums)
        # cnt = Counter(nums)
        d = {i: v for i, v in enumerate(nums)}
        
        res = [0] * N
        helper = defaultdict(int)
        
        nums.sort()
        
        for i, n in enumerate(nums):
            if n in helper:
                continue
            helper[n] = i
        
        for key, value in d.items():
            number = helper[value]
            res[key] = number
        
        return res
            