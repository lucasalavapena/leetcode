class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*collections.Counter(deck).values()) != 1