class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows = 0
        cnt = Counter(secret)
        not_matched = []
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                if g in cnt:
                    cnt[g] -= 1
                    if cnt[g] == 0:
                        del cnt[g]
            else:
                not_matched.append(g)
        
        for nm in not_matched:
            if nm in cnt:
                cows += 1
                cnt[nm] -= 1
                if cnt[nm] == 0:
                    del cnt[nm]
                
        return f"{bulls}A{cows}B"