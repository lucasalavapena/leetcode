class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count, l_count = 0, 0
        total = 0
        for c in s:
            match c:
                case "R":
                    r_count += 1
                case "L":
                    l_count += 1
            if r_count == l_count:
                total += 1
                r_count, l_count = 0, 0
        return total
            