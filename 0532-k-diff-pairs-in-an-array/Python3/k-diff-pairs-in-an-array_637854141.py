from math import comb

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        
        res = 0
        if k != 0:
            sol = set()
            for num, freq in cnt.items():
                if num - k in cnt and (num -k, num) not in sol:
                    sol.add((num -k, num))

                if num + k in cnt and (num, num + k) not in sol:
                    sol.add((num, num + k))
            return len(sol)
        else:
            # 1 ,1, 1
            for num, freq in cnt.items():
                if freq > 1:
                    res +=  1
            return res
            
        
        