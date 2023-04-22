class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
   
        s_d = defaultdict(int)
        g_d = defaultdict(int)

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_d[s] += 1
                g_d[g] += 1
                
        for k, v in s_d.items():
            if k in g_d:
                cows += min(v, g_d[k])
            
        return f"{bulls}A{cows}B"