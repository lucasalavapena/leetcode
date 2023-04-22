class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_size = 0
        
        for key in c:
            if key + 1 in c:
                max_size = max(max_size, c[key] + c[key + 1])
        return max_size