class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1, max(num//2, 1)
        
        while l <= r:
            mid = (l + r)//2
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False