from collections import deque

class Solution:
    def combinations(self, x):        
        for i in range(len(x)):
            yield x[:i] + str((int(x[i]) -1) % 10) + x[i + 1:]
            yield x[:i] + str((int(x[i]) +1) % 10) + x[i + 1:]
                       
    def openLock(self, deadends: List[str], target: str) -> int:
        def upString(string, i):
            string = list(string)
            if string[i] == '9':
                string[i] = '0'
            else:
                string[i] = str(int(string[i]) + 1)
            return ''.join(string)
                
        def downString(string, i):
            string = list(string)
            if string[i] == '0':
                string[i] = '9'
            else:
                string[i] = str(int(string[i]) - 1)
            return ''.join(string)
                
        q1, q2 = {"0000"}, {target}
        dead, visited = set(deadends), set()
        step = 0
        
        while q1 and q2:
            if len(q1) > len(q2):
                q2, q1 = q1, q2
            temp = set()
            for node in q1:
                if node in dead:
                    continue
                if node in q2:
                    return step
                visited.add(node)
                for i in range(4):
                    up_str = upString(node, i)
                    down_str = downString(node, i)
                    if up_str not in visited:
                        temp.add(up_str)
                    if down_str not in visited:
                        temp.add(down_str)
            step += 1
                
            q1 = temp
        
        return -1