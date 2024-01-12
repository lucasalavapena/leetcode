class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set([(0, 0)])
        x, y = 0, 0
        for p in path:
            if p == "N":
                x -= 1
            elif p == "W":
                y -= 1
            elif p == "E":
                y += 1
            elif p == "S":
                x += 1
            if (x, y) in seen: return True
            seen.add((x, y))
        return False