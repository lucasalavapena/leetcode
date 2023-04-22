class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [0] * (n)
        right = [0] * (n)
        
        for i, s in enumerate(seats):
            if s == 1:
                left[i] = 0
            else:
                if i == 0:
                    left[i] = 1
                else:
                    left[i] = left[i-1] + 1
        
        for i in range(n-1,-1, -1):
            if seats[i] == 1:
                right[i] = 0
            else:
                if i == n-1:
                    right[i] = 1
                else:
                    right[i] = right[i+1] + 1

        
        max_dist = 0
        max_idx = 0
        # print(left, right)
        for i in range(0, n):
            if i == n-1 and seats[i] == 0:
                right[i] = left[i]
                
            if i == 0 and seats[i] == 0:
                left[i] = right[i]
                
            if ( dist := min(left[i], right[i])) > max_dist:
                max_dist = dist
                max_idx = i
        
        
        return max_dist