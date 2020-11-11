class Solution:
    def placeJob(self, prev, jobid, daymax, daysleft, jobDifficulty, d):
        if (jobid, daymax, daysleft) in self.mem:
            return prev + self.mem[(jobid, daymax, daysleft)]
        if jobid == len(jobDifficulty):
            if daysleft != 0:
                self.mem[(jobid, daymax, daysleft)] = float("inf")
                return float("inf")
            self.mem[(jobid, daymax, daysleft)] = daymax
            return prev + daymax
        if daysleft == 0:
            newdaymax = max(daymax, max(jobDifficulty[jobid:]))
            self.mem[(jobid, daymax, daysleft)] = newdaymax
            return prev + newdaymax
        if len(jobDifficulty) - jobid < daysleft:
            self.mem[(jobid, daymax, daysleft)] = float("inf")
            return float("inf")
        a = self.placeJob(prev, jobid + 1, max(daymax, jobDifficulty[jobid]), daysleft, jobDifficulty, d)
        b = self.placeJob(prev + daymax, jobid + 1, jobDifficulty[jobid], daysleft-1, jobDifficulty, d)
        if a < b:
            self.mem[(jobid, daymax, daysleft)] = a - prev
            return a
        else:
            self.mem[(jobid, daymax, daysleft)] = b - prev
            return b
        
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        self.mem = dict()
        return self.placeJob(0, 1, jobDifficulty[0], d-1, jobDifficulty, d)        