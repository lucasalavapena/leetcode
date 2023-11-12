class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        current = 1
        res = []

        for t in target:
            diff = t - current 
            res += ["Push", "Pop"] * diff + ["Push"]
            current = t + 1
        return res