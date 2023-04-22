class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = min(weights), sum(weights)
        # print(l, r)
        finalResult = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if self.isPossibility(mid, weights, days):
                finalResult = mid
                r = mid-1
            else:
                l = mid+1
        return finalResult
    
    def isPossibility(self, val, weights, day):
        n = 0
        res = []
        i = 0
        N = len(weights)
        while n < day and i < N:
            curr_sum = 0
            while i < N and curr_sum + weights[i] <= val:
                res.append(weights[i])
                curr_sum += weights[i]
                i += 1
            n += 1
        # print(f"{val=} {weights=} {res=}")
        return len(weights) == len(res)
        
        