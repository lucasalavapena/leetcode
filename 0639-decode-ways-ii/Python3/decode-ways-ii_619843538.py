class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)      
        if s[0] == "0": return 0
        
        dp, dp1 = 0, 1
        
        for i in range(n-1, -1, -1):
            if i + 2 < n + 1:
                if "*" == s[i]:
                    if s[i + 1] != "0":
                        dp += 9 * dp1
                elif s[i] != "0":
                    dp += dp1
                
                if "*" == s[i] and s[i + 1] != "*":
                    if s[i + 1] <= "6":
                        dp += 2 * dp2
                    else:
                        dp += dp2
                elif "*" != s[i] and s[i + 1] == "*" and s[i] <= "2":
                    if s[i] == "1":
                        dp += 9 * dp2
                    elif s[i] == "0":
                        dp += 0 
                    else:
                        dp += 6 * dp2
                elif "*" == s[i] and s[i + 1] == "*" :
                    dp += 15 * dp2
                    
                elif s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    dp += dp2
            else:
                if "*" == s[i]:
                    dp += 9 * dp1
                elif s[i] != "0":
                    dp += dp1
            dp, dp1, dp2 = 0, dp, dp1
            
        return dp1 % (1000000000 + 7)
        
