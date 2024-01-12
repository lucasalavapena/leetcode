import numpy as np
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = np.array(mat)
        cols = [np.sum(m[:, j]) for j in range(m.shape[1])]
        count = 0
        for i in range(m.shape[0]):
            if np.sum(m[i]) == 1:
                idx = np.nonzero(m[i])[0][0]
                if cols[idx] == 1:
                    count += 1
        return count
        