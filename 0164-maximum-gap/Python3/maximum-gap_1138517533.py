class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n_min = min(nums)
        n_max = max(nums)
        N = len(nums)
        range_ = n_max - n_min
        if n_max == n_min or N == 2: return range_
        bucket = defaultdict(list)
        bucket_size = ceil(range_/N) # in each bucket we can contain up to N nodes, 
        for n in nums:
            b_index = (n - n_min)// bucket_size
            bucket[b_index].append(n)
        cands = [[min(bucket[i]), max(bucket[i])] for i in range(N+1) if bucket[i]]
        return max(b[0] - a[1] for a, b in pairwise(cands)) if len(cands) > 1 else range_




                