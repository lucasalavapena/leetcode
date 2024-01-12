class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        N = len(rolls)
        cnt = [0] * k
        res = 0
        unique_ending_die_poss = 0
        for i, r in enumerate(rolls):
            if cnt[r-1] == res:
                cnt[r-1] = res + 1
                unique_ending_die_poss += 1
                if unique_ending_die_poss == k: 
                    res += 1
                    unique_ending_die_poss = 0
        return res + 1