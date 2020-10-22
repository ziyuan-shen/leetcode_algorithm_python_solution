class Solution:
    def cal(self, prev, rem):
        if (prev, rem) in self.mem:
            return self.mem[(prev, rem)]
        elif rem == 0:
            self.mem[(prev, rem)] = 1
            return 1
        else:
            ans = 0
            for i in self.dic[prev]:
                ans += self.cal(i, rem - 1)
            self.mem[(prev, rem)] = ans
            return ans
                
    def numOfWays(self, n: int) -> int:
        self.dic = {1: [2, 3, 5, 6, 11], 2: [1, 4, 7, 9, 12], 3: [1, 4, 7, 8], 4: [2, 3, 8, 11], 5: [1, 7, 9, 10], 6: [1, 7, 8, 10, 11], 7: [2, 3, 5, 6, 12], 8: [3, 4, 6, 12], 9: [2, 5, 10, 11], 10: [5, 6, 9, 12], 11: [1, 4, 6, 9, 12], 12: [2, 7, 8, 10, 11]}
        self.mem = dict()
        ans = 0
        for i in range(1, 13):
            ans += self.cal(i, n - 1)
        return ans % (10 ** 9 + 7)