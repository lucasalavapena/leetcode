class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
        }
        
        x_cord = d[coordinates[0]]
        y_cord = int(coordinates[1])
        if (x_cord + y_cord) % 2 == 0:
            return False
        return True