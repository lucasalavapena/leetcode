class Solution:
    def numberOfWays(self, corridor: str) -> int:
        PRIME = 10**9 + 7
        chair_idx = []
        total = 0
        start = None

        for i, c in enumerate(corridor):
            if c == "S":
                total += 1
                if start is None:
                    start = i 

                if total and total % 2 == 0:
                    chair_idx.append((start, i))
                    start = None

        # if impossible
        if total == 0 or total % 2: return 0
        NC = len(chair_idx)

        res = 1

        for i in range(1, NC):
            res = (res * (chair_idx[i][0] - chair_idx[i-1][1])) % PRIME

        return res