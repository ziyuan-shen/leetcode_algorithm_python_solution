from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.route_count = defaultdict(int)
        self.route_sum = defaultdict(int)
        self.checkins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, start_time = self.checkins[id]
        self.route_count[(startStation, stationName)] += 1
        self.route_sum[(startStation, stationName)] += (t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.route_count:
            return self.route_sum[(startStation, endStation)] / self.route_count[(startStation, endStation)]
        return None


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)