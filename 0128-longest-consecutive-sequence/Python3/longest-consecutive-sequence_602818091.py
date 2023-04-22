class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        
        max_consecutive = 0
        
        for i, k in enumerate(sorted(c)):
            if max_consecutive > len(c)- i:
                return max_consecutive
            
            count = 1
            while c.get(k + count, None) is not None:
                count += 1
            max_consecutive = max(max_consecutive, count)
        return max_consecutive