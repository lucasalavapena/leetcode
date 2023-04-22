class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        cnt, ans = collections.Counter(A), 0
        for i in cnt:
            for j in cnt:
                k = target - i - j
                if i == j == k:
                    ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
                elif i == j:
                    ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[k]
                elif i < j < k:
                    ans += cnt[i] * cnt[j] * cnt[k]
        return ans % (10**9 + 7)