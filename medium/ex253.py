import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        intervals = sorted(intervals)
        rooms = [intervals[0][1]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= rooms[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval[1])
            else:
                heapq.heappush(rooms, interval[1])
        return len(rooms)
            