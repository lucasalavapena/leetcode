import numpy as np
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = np.array(list(map(int, list(boxes))))
        answer = np.zeros(len(boxes), dtype=int)
        for i in range(len(answer)):
            dis = np.array([abs(j - i) for j in range(len(boxes))])
            answer[i] = np.sum(dis * boxes)
        return answer
# slow solution        
        # answer = [0] * len(boxes)
        # for i in range(len(boxes)):
        #     for j, b_str in enumerate(boxes):
        #         if i != j and int(b_str) == 1:
        #             answer[i] += abs(i - j)
        # return answer