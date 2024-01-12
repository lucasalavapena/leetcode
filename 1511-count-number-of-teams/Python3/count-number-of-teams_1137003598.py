class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        ans = 0
        for j in range(1, N-1):
            cand = rating[j]

            i_smaller = 0
            i_greater = 0
            # 1 or 2
            for i in range(j):
                if rating[i] < cand: i_smaller += 1
                elif rating[i] > cand: i_greater += 1
    
            k_smaller = 0
            k_greater = 0
            for k in range(j+1, N):
                if rating[k] < cand: k_smaller += 1
                elif rating[k] > cand: k_greater += 1
            ans += i_smaller * k_greater + i_greater * k_smaller
        return ans