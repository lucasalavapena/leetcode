class UndergroundSystem:

    def __init__(self):
        self.id_start = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_start[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self.id_start[id] 
        if (start_station, stationName) in self.times:
            total, n = self.times[(start_station, stationName)]
        else:
            total, n = 0, 0
        self.times[(start_station, stationName)] = (total + (t - start_t), n + 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, n = self.times[(startStation, endStation)]
        return total/n


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)