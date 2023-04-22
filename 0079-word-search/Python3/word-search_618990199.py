from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        possible = False
        rows = len(board)
        columns = len(board[0])
        
        # is possible because of letters:
        c = Counter(word)
        board_c = Counter(list(chain(*board)))
        for i in c:
            if c[i] > board_c[i]:
                return False
        
        
        x_dir = [-1, 1, 0, 0]
        y_dir = [0, 0, -1, 1]
        
        starting_idxs = [((i, j), 1, set(())) for i in range(rows) for j in range(columns) if board[i][j] == word[0]]
        q = deque(starting_idxs)
        
        while q:
            (i, j), word_idx, visited = q.popleft()
            new_visited = {v for v in visited}
            new_visited.add((i, j))
            
            
            
            if word_idx == len(word):
                return True
            
            for n in range(4):
                new_i, new_j = i + x_dir[n], j + y_dir[n]
                if 0 <= new_i < rows and 0 <= new_j < columns and board[new_i][new_j] == word[word_idx] and (new_i, new_j) not in new_visited:  
                    q.append(((new_i, new_j), word_idx + 1, new_visited))
        
        return possible