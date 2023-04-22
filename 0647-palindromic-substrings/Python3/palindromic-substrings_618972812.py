class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i + 1, n+1):
                string = s[i:j]
                if string == string[::-1]:
                    count += 1 
        
        return count