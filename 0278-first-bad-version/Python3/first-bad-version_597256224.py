# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, upper = 0, n
        
        while low <= upper:
            mid = (low + upper) // 2
            
            status = isBadVersion(mid)
            if status:
                upper = mid - 1
            else:
                low = mid + 1
        return low