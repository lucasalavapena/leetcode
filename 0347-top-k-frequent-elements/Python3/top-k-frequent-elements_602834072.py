class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [w for w, count in Counter(nums).most_common(k)]
        
        
        