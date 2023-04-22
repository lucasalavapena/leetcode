class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        res = [0]
        n = len(nums)
        prev = max_score = sum(nums)
        
        for i in range(1, n+1):
            score = prev + int(nums[i-1] == 0) - int(nums[i-1] == 1)
            if score > max_score:
                res = [i]
                max_score = score
            elif score == max_score:
                res.append(i)
            prev = score
        return res
                