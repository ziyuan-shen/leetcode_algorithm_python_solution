class Solution:
    def findDifference(self, point1, point2):
        h1 = point1[:2]
        if h1[0] == '0':
            h1 = h1[1]
        h1 = int(h1)
        m1 = point1[3:]
        if m1[0] == '0':
            m1 = m1[1]
        m1 = int(m1)
        h2 = point2[:2]
        if h2[0] == '0':
            h2 = h2[1]
        h2 = int(h2)
        m2 = point2[3:]
        if m2[0] == '0':
            m2 = m2[1]
        m2 = int(m2)
        time1 = h1 * 60 + m1
        time2 = h2 * 60 + m2
        diffmin = abs(time1 - time2)
        return min(diffmin, 24 * 60 - diffmin)
        
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        diffs = []
        for i in range(len(timePoints)-1):
            diffs.append(self.findDifference(timePoints[i], timePoints[i+1]))
        diffs.append(self.findDifference(timePoints[0], timePoints[-1]))
        return min(diffs)