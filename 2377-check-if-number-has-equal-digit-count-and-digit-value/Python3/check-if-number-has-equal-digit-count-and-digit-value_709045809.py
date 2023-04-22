class Solution:
    def digitCount(self, num: str) -> bool:
        
        cnt = Counter(num)
        
        for i, n in enumerate(num):
            if int(n) != cnt[str(i)]:
                return False
    
        return True