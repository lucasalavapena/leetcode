class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        
        prev = None
        start = nums[0]
        for n in nums + [float("inf")]:
            if prev is not None:
                if n != prev + 1:
                    if start != prev:
                        res.append(f"{start}->{prev}")
                    else:
                        res.append(f"{start}")
                    start = n
            prev = n
        return res