class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # taken form runtime analysis
        # use indexes, this could save us memory? and avodi non zero
        choices = sorted(
            (i for i in range(len(profits)) if profits[i]),
            key=lambda i: profits[i],
            reverse=True,
        )

        while choices and k:
            for cidx, i in enumerate(choices):
                if capital[i] <= w:
                    w += profits[i]
                    k -= 1
                    del choices[cidx]
                    break
            else:
                break
            
        return w
