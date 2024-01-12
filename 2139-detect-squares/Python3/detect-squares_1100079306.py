from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.by_x_axis = defaultdict(set)
        self.by_y_axis = defaultdict(set)
        self.pointer_counter = defaultdict(int)


    def add(self, point: List[int]) -> None:
        x, y = point

        self.by_x_axis[x].add(y)
        self.by_y_axis[y].add(x)

        self.pointer_counter[(x, y)] += 1


    def count(self, point: List[int]) -> int:
        total = 0
        x, y = point

        for cand_y in self.by_x_axis[x]:
            square_side = abs(y - cand_y)

            if square_side == 0:
                continue

            # left
            left_x = x-square_side

            if y in self.by_x_axis[left_x] and cand_y in self.by_x_axis[left_x]:
                total += self.pointer_counter[(x, cand_y)] * self.pointer_counter[(left_x, y)] * self.pointer_counter[(left_x, cand_y)]

            right_x = x+square_side

            if y in self.by_x_axis[right_x] and cand_y in self.by_x_axis[right_x]:
                total += self.pointer_counter[(x, cand_y)] * self.pointer_counter[(right_x, y)] * self.pointer_counter[(right_x, cand_y)]

        return total


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)