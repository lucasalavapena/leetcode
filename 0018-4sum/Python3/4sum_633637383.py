class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []      
        sol = set()
        seen = defaultdict(int)
        
        for n in nums:
            for k, v in seen.items():
                for k2 in seen:
                    # 
                    # print(n, k, k2)
                    remaining = target-(n + k + k2)
                    if remaining in seen:
                        if (remaining == k and seen[remaining] <= 1) or (remaining == k2 and seen[remaining] <= 1) or (k == k2 and v <= 1) or (remaining == k2 and remaining == k and seen[remaining] <= 2):
                            continue
                        else:
                            i, j, c, m = sorted([n, k, remaining, k2])

                            if (i, j, c, m) not in sol:
                                res.append([i, j, c, m])
                                sol.add((i, j, c, m))
            
            seen[n] += 1
        
        return res