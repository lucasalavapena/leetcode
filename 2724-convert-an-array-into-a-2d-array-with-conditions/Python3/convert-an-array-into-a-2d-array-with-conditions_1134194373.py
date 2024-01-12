class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        res = []
        while cnt:
            row = []
            for k in list(cnt):
                row.append(k)
                cnt[k] -= 1
                if cnt[k] == 0: del cnt[k]
            res.append(row)
        return res