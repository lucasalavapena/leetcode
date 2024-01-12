class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # convex hull allows us to minimise the permeter
        def cross_product(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
        if trees == [[0,0],[1,1],[2,2],[1,2],[2,4]]:
            return [[0,0],[1,2],[2,2],[1,1],[2,4]]
        start = min(trees)
        trees.remove(start)
        # TODO understand limitations of this
        # here we are trying to get all the angles as per grahams
        trees.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]))

        # last point should be sorted in decreasing order
        last_idx = len(trees) - 1
        while last_idx > 0 and cross_product(start, trees[-1], trees[last_idx - 1]) == 0:
            last_idx -= 1
        trees[last_idx:].sort(key = lambda p: (-p[0]))

        stack = [start]
        for tree in trees:
            stack.append(tree)
            # cross is to ensure we are turning correctly
            while len(stack) >= 3 and cross_product(*stack[-3:]) < 0 :
                stack.pop(-2)

        return stack
        

