class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])

        for i, j in product(range(m), range(n)):
            diagonals[i - j].append(mat[i][j])

        for diag in diagonals:
            diagonals[diag] = deque(sorted(diagonals[diag]))

        for i, j in product(range(m), range(n)):
            mat[i][j] = diagonals[i-j].popleft()
        
        return mat