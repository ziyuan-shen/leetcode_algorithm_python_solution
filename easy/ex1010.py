from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        dic = defaultdict(int)
        dic[time[0] % 60] = 1
        for i in range(1, len(time)):
            rem = time[i] % 60
            if rem == 0:
                ans += dic[0]
            else:
                ans += dic[60 - rem]
            dic[rem] += 1
        return ans