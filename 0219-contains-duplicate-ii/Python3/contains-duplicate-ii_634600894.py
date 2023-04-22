class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        reference = defaultdict(list)
        for i, n in enumerate(nums):
            if n in reference:
                latext_idx = reference[n][-1]
                if abs(latext_idx- i) <= k:
                    return True
            reference[n].append(i)
        return False