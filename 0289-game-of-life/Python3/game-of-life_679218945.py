class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        alive = set([(i, j) for i, j in product(range(m), range(n)) if board[i][j] == 1])
        neibs = list(product(range(-1, 2), range(-1, 2)))
        
        cnt = defaultdict(int)
        
        for i, j in alive:
            for dx, dy in neibs:
                cnt[(i + dx,j + dy)] += 1
                
        for x, y in cnt:
            if 0 <= x < m and 0 <= y < n:
                if cnt[x, y] == 3 and board[x][y] == 0: board[x][y] = 1
                if cnt[x, y] not in {3, 4}: board[x][y] = 0