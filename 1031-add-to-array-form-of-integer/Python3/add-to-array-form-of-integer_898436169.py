class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(r) for r in str(int("".join(str(s) for s in num)) + k)]