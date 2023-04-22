class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []      
        sol = set()
        seen = defaultdict(int)
        
        for n in nums:
            for k, v in seen.items():
                remaining = -(n + k)
                if remaining in seen:
                    if remaining == k and seen[remaining] <= 1:
                        continue
                    else:
                        i, j, k = sorted([n, k, remaining])
         
                        if (i, j, k) not in sol:
                            res.append([i, j, k])
                            sol.add((i, j, k))
            
            seen[n] += 1
        
        return res