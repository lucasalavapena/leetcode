class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        cnt = Counter()
        
        for line in wall:
            for place in list(accumulate(line))[:-1]:
                cnt[place] += 1
                
        return len(wall) - max(cnt.values()) if cnt else len(wall)