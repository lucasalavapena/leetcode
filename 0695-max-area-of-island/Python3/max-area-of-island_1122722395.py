# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         q = collections.deque([(i, j, 1) for j in range(n) for i in range(m) if grid[i][j]])
#         seen = {(i, j): 1 for j in range(n) for i in range(m) if grid[i][j]]}
#         max_area = 0
#         count = -1

#         while q:
#             q_len = len(q)
#             count += 1
#             for _ in range(q_len):
#                 x, y = q.popleft()

#                 for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                     nx, ny = x + dx, y + dy
#                     if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:


#         return 19

class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [1] * N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr: return
        if self.rank[xr] > self.rank[yr]:
            self.p[yr] = xr
            self.rank[xr] += self.rank[yr]
            self.rank[yr] = 0
        else:
            self.p[xr] = yr
            self.rank[yr] += self.rank[xr]
            self.rank[xr] = 0


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = DSU(m * n)
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cnt += 1
                    if 0 <= j-1 and grid[i][j-1]:
                        d.union(j + i * n, j - 1 + i * n)
                    if 0 <= i-1 and grid[i-1][j]:
                        d.union(j + (i-1) * n, j + i * n)
                    if i + 1 < m and grid[i+1][j]:
                        d.union(j + (i+1) * n, j + i * n)
                    if j + 1 < n and grid[i][j+1]:
                        d.union(j + 1 + i * n, j + i * n)

        max_count = max(d.rank)
        return max_count if max_count >= 1 and cnt else 0
