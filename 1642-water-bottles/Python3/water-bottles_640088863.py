class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        curr, res= numBottles, 0   
        remaining = 0
        while curr > 0:
            res += curr
            curr += remaining
            remaining =  curr % numExchange
            curr = curr//numExchange
        return res