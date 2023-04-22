class TimeMap:
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''


    
    def binary_search(self, key, timestamp):
        
        beg, end = 0, len(self.info[key])-1
        while beg < end:
            mid = (beg + end)//2
            print(beg, end, self.info[key], timestamp, self.info[key][mid][0])
            if self.info[key][mid][0] == timestamp:
                return mid
            elif self.info[key][mid][0] < timestamp:
                beg = mid 
            else:
                end = mid -1
        
        return end


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)