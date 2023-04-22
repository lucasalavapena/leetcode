class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for a in arr:
            if a % 2 == 0:
                cnt = 0
            else:
                cnt += 1
                if cnt == 3:
                    return True
        return False
                    