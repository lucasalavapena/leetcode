from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if not board:
            return 0

        n = len(board)
        # convert the label/num to position (x, y) in a mtrix
        def label_to_pos(label):
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c

        visited = set()
        queue = collections.deque([(1, 0)])
        # bfs to until the label n*n and return the step. 
        while queue:

            label, step = queue.popleft()

            for nxt_label in range(label+1, label+7):
                r, c = label_to_pos(nxt_label)

                if board[r][c] > 0:
                    nxt_label = board[r][c]

                if nxt_label == n*n:
                    return step + 1

                if nxt_label not in visited:
                    visited.add(nxt_label)
                    queue.append((nxt_label, step + 1))
        return -1


            
            
            