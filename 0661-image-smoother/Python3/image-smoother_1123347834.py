class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        def get_neighbours(x, y):
            for nx, ny in [(x-1,y-1), (x-1, y), (x-1, y+1), (x, y-1),(x, y), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    yield img[nx][ny]

        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                neigh = list(get_neighbours(i, j))
                res[i][j] = sum(neigh)//len(neigh)
        return res