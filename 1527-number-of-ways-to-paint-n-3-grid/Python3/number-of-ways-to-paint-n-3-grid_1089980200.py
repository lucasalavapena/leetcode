class Solution:
    def numOfWays(self, n: int) -> int:
        """
        start: 
        c1, c2, c1

        c2, c1, c2,
        c3, c1, c3
        c2, c3, c2

        c2, c1, c3
        c3, c1, c2


        start: 
        c1, c2, c3

        c2 c1 c2
        c2 c3 c2
        
        c2 c3 c1
        c3 c1 c2
        """
        PRIME = 10**9 + 7
        two_color, three_color = 6, 6
        for i in range(1, n):
            three_color, two_color =  (2 * two_color + 2 * three_color) % PRIME, (3 * two_color + 2 * three_color) % PRIME
        return (three_color + two_color) % PRIME