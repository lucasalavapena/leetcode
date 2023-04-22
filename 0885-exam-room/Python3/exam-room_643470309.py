class ExamRoom:

    def __init__(self, n: int):
        self.stack=[(n, -1 ,n)]
        self.visit={-1:[-1,n],n:[-1,n]}
        self.n=n
        

    def seat(self) -> int: 
        
        while (self.stack[0][1] not in self.visit) or (self.visit[self.stack[0][1]][1]!=self.stack[0][2]):
            heapq.heappop(self.stack)

        _,l,r=heapq.heappop(self.stack)
        if l<0:
            mid=0
            heapq.heappush(self.stack,(-((r-mid-2)//2),mid,r))
            
        elif r==self.n:
            mid=self.n-1
            heapq.heappush(self.stack,(-((mid-2-l)//2),l,mid))

        else:
            mid=(l+r)//2    
            heapq.heappush(self.stack,(-((mid-2-l)//2),l,mid))
            heapq.heappush(self.stack,(-((r-mid-2)//2),mid,r))

        self.visit[mid]=[l,r]
        self.visit[l][1]=self.visit[r][0]=mid
        return mid

        
    def leave(self, p: int) -> None:
        l,r=self.visit[p]
        
        self.visit[l][1]=r
        self.visit[r][0]=l
        
        heapq.heappush(self.stack,(-(r-l-2),l,r))
        self.visit.pop(p)