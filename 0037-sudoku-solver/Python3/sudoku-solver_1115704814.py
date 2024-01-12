from copy import deepcopy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, empty, i, rows, cols, boxes):
            if i == len(empty): return True
            r, c = empty[i]
            for k in set("123456789") - (rows[r]|cols[c]|boxes[3*(r//3)+c//3]):
                board[r][c] = k
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(k)
                if dfs(board, empty, i+1, rows, cols, boxes): return True
                board[r][c] = '.'
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.remove(k)

            return False
        
        cols, rows, boxes, empty = defaultdict(set), defaultdict(set), defaultdict(set), []
        for r, c in product(range(9), range(9)):
            if board[r][c] == ".":
                empty.append((r,c))
            else:
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(board[r][c])
                
        dfs(board, empty, 0, rows, cols, boxes)


            
