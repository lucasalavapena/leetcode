class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.graph = defaultdict(set)
        
        for course, prerequisites in prerequisites:
            self.graph[prerequisites].add(course)
            
        self.state = [0] * numCourses
        self.has_cycle = False
        
        for i in range(numCourses):
            if not self.state[i]:
                self.dfs(i)
            if self.has_cycle:
                return False
        
        return True
        
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
