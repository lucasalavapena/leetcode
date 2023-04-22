class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True

        self.graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            self.graph[prerequisite].add(course)

        self.visited = [0] * numCourses
        self.FoundCycle = 0
        
        for i in range(numCourses):
            if self.FoundCycle == 1: return False
            
            if self.visited[i] == 0:
                self.dfs(i)
        
        return self.FoundCycle == 0
    
    def dfs(self, curr):
        if self.FoundCycle == 1: return
        if self.visited[curr] == 1: 
            self.FoundCycle = 1
        if self.visited[curr] == 0: 
            self.visited[curr] = 1
            for neigh in self.graph[curr]:
                self.dfs(neigh)
            self.visited[curr] = 2
                    