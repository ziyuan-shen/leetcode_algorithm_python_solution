class Solution:
    def binarySearch(self, low, target):
        high = len(self.starts) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.starts[mid] < target:
                low = mid + 1
            elif mid == low or self.starts[mid-1] < target:
                return mid
            else:
                high = mid - 1
        return -1
        
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort()
        dp = [0 for _ in range(len(jobs))]
        dp2 = [0 for _ in range(len(jobs))]
        dp2[-1] = jobs[-1][2]
        self.starts = [job[0] for job in jobs]
        for idx in range(len(jobs)-1, -1, -1):
            dp[idx] = jobs[idx][2]
            next_idx = self.binarySearch(idx+1, jobs[idx][1])
            if next_idx != -1:
                dp[idx] += dp2[next_idx]
            if idx != len(jobs) - 1:
                dp2[idx] = max(dp[idx], dp2[idx+1])
        return dp2[0]