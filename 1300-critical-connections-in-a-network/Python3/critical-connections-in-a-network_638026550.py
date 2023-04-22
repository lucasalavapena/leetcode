class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        used, tin, fup = [0]*n, [-1]*n, [-1]*n
        self.timer, ans = 0, []
        graph = defaultdict(list)
        
        def dfs(node, parent=None):
            used[node] = 1
            self.timer += 1
            fup[node] = tin[node] = self.timer
            
            for child in graph[node]:
                if child == parent:
                    continue
                if used[child]:
                    fup[node] = min(fup[node], tin[child])
                else:
                    dfs(child, node)
                    fup[node] = min(fup[node], fup[child])
                    if fup[child] > tin[node]:
                        ans.append([node, child])
            
        
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            
        for i in range(n):
            if not used[i]: dfs(i)
                
        return ans
        
        
        