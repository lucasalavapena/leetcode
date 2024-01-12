class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        N = len(nums)
        idxs = [-1]+[i for i, v in enumerate(nums) if v==max_val]
        if len(idxs)-1 < k: return 0
        return sum((idxs[i] - idxs[i-1])*(N-idxs[i+k-1])for i in range(1, len(idxs)-k+1))