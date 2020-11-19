from collections import defaultdict
from bisect import bisect
class TweetCounts:

    def __init__(self):
        self.timedict = defaultdict(set)
        self.countlist = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.timedict:
            if time in self.timedict[tweetName]:
                idx = bisect(self.countlist[tweetName], [time, 0])
                self.countlist[tweetName][idx][1] += 1
            else:
                self.timedict[tweetName].add(time)
                idx = bisect(self.countlist[tweetName], [time, 1])
                self.countlist[tweetName].insert(idx, [time, 1])
        else:
            self.timedict[tweetName].add(time)
            self.countlist[tweetName].append([time, 1])
            
    def getTweetCountByInterval(self, tweetName, start, end):
        if tweetName not in self.timedict:
            return 0
        counts = self.countlist[tweetName]
        idx1 = bisect(counts, [start, 0])
        idx2 = bisect(counts, [end, 0])
        return sum([l[1] for l in counts[idx1:idx2]])

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 60 * 60
        else:
            interval = 60 ** 3
        intervals = []
        while startTime <= endTime:
            intervals.append([startTime, min(endTime + 1, startTime + interval)])
            startTime = min(endTime + 1, startTime + interval)
        ans = [0 for _ in range(len(intervals))]
        for idx in range(len(intervals)):
            ans[idx] = self.getTweetCountByInterval(tweetName, intervals[idx][0], intervals[idx][1])
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)