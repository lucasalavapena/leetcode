class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        goal = str([[0] * n for _ in range(m)])
        if str(mat) ==goal: return 0
        q  = deque([mat])
        seen = set(str(mat))
        moves = -1
        while q:
            q_len = len(q)
            moves += 1
            for _ in range(q_len):
                state = q.popleft()
                for i in range(m):
                    for j in range(n):
                        cand_state = [row[:] for row in state]
                        cand_state[i][j] ^= 1
                        if i-1 >=0: cand_state[i-1][j] ^= 1
                        if j-1 >=0: cand_state[i][j-1] ^= 1
                        if i+1 < m: cand_state[i+1][j] ^= 1
                        if j+1 < n: cand_state[i][j+1] ^= 1
                        if str(cand_state) not in seen:
                            seen.add(str(cand_state))
                            q.append(cand_state)
                            if str(cand_state) == goal: return moves+1

        return -1
