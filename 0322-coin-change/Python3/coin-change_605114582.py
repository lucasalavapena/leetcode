from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeHelper(coins, amount, {})
    
    def coinChangeHelper(self, coins: List[int], amount_remaining: int , memo: dict={}):

        if amount_remaining in memo:
            return memo[amount_remaining]
        if amount_remaining == 0:
            return 0
        if amount_remaining < 0:
            return -1
        
        res = -1
        for c in coins:
            prev_path = self.coinChangeHelper(coins , amount_remaining - c, memo)
            if prev_path != -1:
                curr_path = prev_path + 1
                
                if res == -1 or curr_path < res:

                    res = curr_path
            
        memo[amount_remaining] = res
        return res
        
        
        
        