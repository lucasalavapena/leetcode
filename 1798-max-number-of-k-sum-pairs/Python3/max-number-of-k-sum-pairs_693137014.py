class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        
        for key in cnt:
            required = k - key
            if required in cnt:
                if required == key:
                    times = cnt[key]//2
                    cnt[key] = 0
                else:
                    times = min(cnt[required], cnt[key])
                    cnt[required] -= times
                    cnt[key] -= times
                ans += times
        return ans