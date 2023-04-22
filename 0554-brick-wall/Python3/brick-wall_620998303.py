class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        rows = len(wall)
        cols = len(wall[0])
        
        position_free = Counter()
        
        for r in range(rows):
            total = 0
            for j in wall[r]:
                total += j
                position_free[total] += 1
        
        if len(position_free) == 1:
            return rows
        else:
            loc, count = position_free.most_common(2)[1]
            # print(loc, count, position_free.most_common(2), rows)
        return rows - count