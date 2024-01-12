# class BIT2D:
#     def __init__(self, nx, ny):
#         self.nx = nx + 1
#         self.ny = ny + 1
#         self.sums = [[0] * self.ny for i in range(self.nx)]

#     def update(self, x, y, delta):
#         while x < self.nx:
#             curr_y = y
#             while curr_y < self.ny:
#                 self.sums[x][curr_y] += delta
#                 curr_y += curr_y & (-curr_y)
#             x += x & (-x)
    
#     def query_covering(self, x, y):
#         res = 0
#         while 0 < x:
#             curr_y = y
#             while 0 < curr_y:
#                 res += self.sums[x][curr_y]
#                 curr_y -= curr_y & (-curr_y)
#             x -= x & (-x)
#         return res

#     def query_inclusive(self, x, y):
#         # we are double subtracting the ones one the lines... we somehow need to make it be exlusive on line
#         return self.query_covering(self.nx-1, self.ny-1) - self.query_covering(x-1, self.ny) - self.query_covering(self.nx-1, y) + self.query_covering(x, y) + 1

class BIT:
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)
        
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution:
        def countRectangles(self, r: List[List[int]], p: List[List[int]]) -> List[int]:
            N, M = len(p), len(r)

            p_index = sorted(range(N), key=lambda x: p[x][0], reverse=True)
            r.sort(reverse=True)

            bit = BIT(100) # to compute ongoing prefix_sum of heights/ys 
            res = [0] * N
            curr_wider = 0 # total rect that are greater or equal in width to our current point
            for p_i in p_index:
                while curr_wider < M and r[curr_wider][0] >= p[p_i][0]:
                    bit.update(r[curr_wider][1] + 1, 1) 
                    curr_wider += 1
                res[p_i] = curr_wider - bit.query(p[p_i][1]) # note: we need to subtract by the heights (y) that are too small (our BIT keeps track of the sum of recetangles less than i in height)
            return res



    # def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
    #     # y is small so no need to worry about its transform
    #     x_only = sorted({x for x,y in rectangles})
    #     N = len(x_only)
    #     bit = BIT2D(N, 100)
    #     for x, y in rectangles:
    #         x_trans = bisect_left(x_only, x) + 1
    #         bit.update(x_trans, y, 1)
    #     print(f"{bit.sums=}")
    #     res = [0] * len(points)
    #     for i, (x, y) in enumerate(points):
    #         x_trans = bisect_left(x_only, x) + 1
    #         print(f"{x=} {x_trans=}")
    #         res[i] = bit.query_inclusive(x_trans, y)
    #     return res