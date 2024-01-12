from collections import defaultdict

class TweetCounts:

    def __init__(self):
        self.data = defaultdict(list)
        self.deltas = {"minute": 60, "hour": 3600, "day": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.deltas[freq]
        res = [0] * ((endTime - startTime)//delta + 1)
        for t in self.data[tweetName]:
            if startTime <= t <= endTime:
                idx = (t - startTime)//delta
                res[idx] += 1
            
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)