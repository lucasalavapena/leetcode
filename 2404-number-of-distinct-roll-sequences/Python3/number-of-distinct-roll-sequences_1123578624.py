class Solution:
    def distinctSequences(self, n: int) -> int:
        PRIME = 1_000_000_007
        D = 6
        dp = [[[0] * (D + 1) for j in range(D + 1)] for i in range(n)]
        
        after = {
            0: [1, 2, 3, 4, 5, 6], # 1: 2, 3,4, 5, 6
            1: [0, 2, 4, 6], # 2: 1, 3, 5
            2: [0, 1, 3, 4, 6], #  3: 1, 2, 4, 5
            3: [0, 2, 4, 6], #  4: 1, 3, 5
            4: [0, 1, 2, 3, 5, 6], # 5: 1, 2, 3, 4, 6
            5: [0, 4, 6], # 6: 1, 5
            6: list(range(6))
        }
        # print(len(dp), len(dp[0]), len(dp[0][0]))
        for dice_roll in range(D):
            dp[0][dice_roll][6] = 1

        for i in range(1, n):
            for dice_roll in range(D):
                for k in after[dice_roll]:
                    for j in after[k]:
                        if j != dice_roll:
                            dp[i][dice_roll][k] += dp[i-1][k][j] % PRIME

        res = 0
        for row in dp[-1]:
            for r in row:
                res = (res + r) % PRIME

        return res