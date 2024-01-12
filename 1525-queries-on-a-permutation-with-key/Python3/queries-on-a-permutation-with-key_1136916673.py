class BIT:
    def __init__(self, n):
        self.sums = [0] * (n + 1) # is 1 indexed

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i) # add least signfcant bit

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i) # sub least signfcant bit
        return res



class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        n = len(queries)
        bit = BIT(m + n)
        coord_map = defaultdict(int)

        """
        creates binary index with a space of n since we will push n stuff to the front!

        """
        for i in range(1, m + 1):
            idx = i + n
            coord_map[i] = idx
            bit.update(idx, 1)

        res = []
        for q in queries:
            # -1 since we need zero index :)
            coord_idx = coord_map[q]
            ans = bit.query(coord_idx) - 1
            res.append(ans)
            # remove count from previous loc
            bit.update(coord_idx, -1)
            # add count to new loc
            bit.update(n, 1)
            # moving it to the front
            coord_map[q] = n
            n -= 1 # do this after since our initial variable is at n + 1

        return res