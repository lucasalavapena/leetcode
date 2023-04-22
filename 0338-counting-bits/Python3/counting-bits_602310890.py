class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f"{i:b}".count("1") for i in range(n+1)]
