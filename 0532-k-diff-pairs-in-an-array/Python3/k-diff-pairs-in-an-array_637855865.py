from math import comb

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        if k != 0:
            cnt = set(nums)
            sol = set()
            for num in cnt:
                if num - k in cnt:
                    res += 1
                if num + k in cnt:
                    res += 1
            return res//2
        else:
            # 1 ,1, 1
            cnt = Counter(nums)
            for num, freq in cnt.items():
                if freq > 1:
                    res +=  1
            return res
            
        
        