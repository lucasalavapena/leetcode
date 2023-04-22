class UndergroundSystem:

    def __init__(self):
        self.id_start = {}
        self.times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_start[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self.id_start[id] 
        self.times[(start_station, stationName)].append(t-start_t)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        entries = self.times[(startStation, endStation)]
        N = len(entries)
        
        return sum(entries)/N


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)