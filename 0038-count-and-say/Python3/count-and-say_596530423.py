class Solution:

            
    
    def countAndSay(self, n: int) -> str:
        
        res = [""] * n
        res[0] = "1"
        
        count = 0
        for i in range(1, n):
            curr = res[i-1]
            prev = curr[0]
            count = 0
            for ni in curr:
                if ni != prev:
                    res[i] += str(count) + str(prev)
                    # print(res[i])
                    count = 0
                count += 1
                prev = ni

            if ni == prev:
                res[i] += str(count) + str(prev)
                # print(res[i])

            # print(res[i])

        return res[-1]