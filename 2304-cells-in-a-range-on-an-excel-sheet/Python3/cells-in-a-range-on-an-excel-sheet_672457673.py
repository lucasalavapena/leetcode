class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        char1, start, _, char2, end = s
        return [chr(i) + str(j) for i in range(ord(char1), ord(char2) + 1) for j in range(int(start), int(end) + 1)]