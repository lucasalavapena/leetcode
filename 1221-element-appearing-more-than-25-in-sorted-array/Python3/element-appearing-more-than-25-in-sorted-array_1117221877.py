from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        cnt = defaultdict(int)
        required =  N // 4
        for a in arr:
            cnt[a] += 1
            if cnt[a] > required: return a
        return -1