from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        DESIRED_STATE = [[1,2,3],[4,5,0]]
        seen_board_states = set()

        zero_loc = [(i,j) for j in range(3) for i in range(2) if board[i][j] == 0][0]

        q = deque([(board, zero_loc)]) 
        count = -1
        DIRS = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        while q:
            q_len = len(q)
            count += 1
            # print(f"{count=} {q=}")
            for _ in range(q_len):
                board_state, (x, y) = q.popleft()

                if board_state == DESIRED_STATE:
                    return count
                seen_board_states.add(str(board_state))

                for (dx, dy) in DIRS:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < 2 and 0 <= new_y < 3:
                        new_board = [item[:] for item in board_state]
                        new_board[x][y] = new_board[new_x][new_y]
                        new_board[new_x][new_y] = 0
                        if str(new_board) in seen_board_states: 
                            continue
                        q.append((new_board, (new_x, new_y)))
        return -1
        
