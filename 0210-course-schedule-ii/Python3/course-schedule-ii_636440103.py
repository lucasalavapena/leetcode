class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            return list(range(numCourses))

        self.graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            self.graph[prerequisite].add(course)

        self.visited = [0] * numCourses
        self.FoundCycle = 0
        self.res = []
        for i in range(numCourses):
            if self.FoundCycle == 1: return []
            
            if self.visited[i] == 0:
                self.dfs(i)
        if self.FoundCycle == 1: return []

        return self.res[::-1]
    
    def dfs(self, curr):
        if self.FoundCycle == 1: return
        if self.visited[curr] == 1: 
            self.FoundCycle = 1
        if self.visited[curr] == 0: 
            self.visited[curr] = 1
            for neigh in self.graph[curr]:
                self.dfs(neigh)
            self.visited[curr] = 2
            self.res.append(curr)
                    
        

        