class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N % k != 0 : return False
        cnt = Counter(nums)
        sorted_keys = sorted(list(cnt))
        
        for key in sorted_keys:
            while key in cnt:
                for required_key in range(key, key + k):
                    if required_key not in cnt:
                        return False
                    else:
                        cnt[required_key] -= 1
                        if cnt[required_key] == 0:
                            del cnt[required_key]                        
    
        return sum(v for k, v in cnt.items()) == 0