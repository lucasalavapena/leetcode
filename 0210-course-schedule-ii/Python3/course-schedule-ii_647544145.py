class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = defaultdict(set)
        
        for course, prerequisites in prerequisites:
            self.graph[prerequisites].add(course)
            
        self.state = [0] * numCourses
        self.has_cycle = False
        self.res = []
        
        for i in range(numCourses):
            if not self.state[i]:
                self.dfs(i)
            if self.has_cycle:
                return []
        
        return self.res[::-1]
        
    def dfs(self, curr):
        if self.has_cycle:
            return
        if self.state[curr] == 1:
            self.has_cycle = True
            return
        
        self.state[curr] = 1
        
        for neigh in self.graph[curr]:
            if self.state[neigh] != 2:
                self.dfs(neigh)
        
        self.state[curr] = 2
        self.res.append(curr)