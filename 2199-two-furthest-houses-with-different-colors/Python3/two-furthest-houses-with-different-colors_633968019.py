class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        extremes = defaultdict(list)
        
        for i, c in enumerate(colors):
            if c not in extremes:
                extremes[c].append(i)
                extremes[c].append(i)
            else:
                extremes[c][1] = i
        
        max_val = 0
        for k, v in extremes.items():
            for k2, v2 in extremes.items():
                if k2 != k:
                    max_val = max(max_val, abs(v[0]-v2[0]), abs(v[1]-v2[0]) , abs(v[0]-v2[1] ), abs(v[1]-v2[1]) )
        return max_val
        
                    
                    