"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def quad_helper(mid_x, mid_y, radius) -> 'Node':
            """
            _________ y
            |
            |
            |
            x


            """
            # print(f"{mid_x=} {mid_y=} {radius=}")
            if radius == 0: return Node(grid[mid_x][mid_y], True, None, None, None, None)
            
            # print(f"{[grid[i][j] for j in range(mid_y-radius, mid_y+radius) for i in range(mid_x-radius, mid_x+radius)]=}")
            # if all
            if all(grid[i][j] for j in range(mid_y-radius, mid_y+radius) for i in range(mid_x-radius, mid_x+radius)):
                node = Node(
                        1,
                        True,
                        None, 
                        None, 
                        None,
                        None
                )
            else:

                if not any(grid[i][j] for j in range(mid_y-radius, mid_y+radius) for i in range(mid_x-radius, mid_x+radius)):
                    # print(f"{mid_x=} {mid_y=} {radius=}")
                    node = Node(
                            0,
                            True,
                            None, 
                            None, 
                            None,
                            None
                    )
                else:
                    new_radius = radius//2
                    # x_offset = mid_x - radius
                    # y_offset = mid_y - radius
                    if new_radius == 0:
                        node = Node(
                                1,
                                False,
                                quad_helper(mid_x - 1, mid_y - 1, new_radius), 
                                quad_helper(mid_x - 1, mid_y, new_radius), 
                                quad_helper(mid_x, mid_y - 1, new_radius),
                                quad_helper(mid_x, mid_y, new_radius)
                        ) 
                    else:
                        node = Node(
                                1,
                                False,
                                quad_helper(mid_x - new_radius, mid_y - new_radius, new_radius), 
                                quad_helper(mid_x - new_radius, mid_y + new_radius, new_radius), 
                                quad_helper(mid_x + new_radius, mid_y - new_radius, new_radius),
                                quad_helper(mid_x + new_radius, mid_y + new_radius, new_radius)
                        ) 


            return node

        
        return quad_helper(n//2, n//2, n // 2)




    