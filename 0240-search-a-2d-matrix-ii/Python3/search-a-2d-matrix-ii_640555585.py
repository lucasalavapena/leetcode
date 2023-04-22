class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix[0]) - 1, 0
        while x >= 0 and y < len(matrix):
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                return True
        return False