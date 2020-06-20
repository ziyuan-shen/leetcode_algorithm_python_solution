from collections import defaultdict
class Solution:
    def move(self, current):
        if len(current) < 9:
            for num in range(1, 10):
                if num not in current:
                    if (current[-1], num) in self.bridgedict:
                        if self.bridgedict[(current[-1], num)] in current:
                            self.patterns[len(current) + 1] += 1
                            self.move(current + (num,))
                    elif (num, current[-1]) in self.bridgedict:
                        if self.bridgedict[(num, current[-1])] in current:
                            self.patterns[len(current) + 1] += 1
                            self.move(current + (num,))
                    else:
                        self.patterns[len(current) + 1] += 1
                        self.move(current + (num,))
            
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.patterns = defaultdict(int)
        self.patterns[1] = 9
        self.bridgedict = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (1, 9): 5, (3, 7): 5}
        for i in range(1, 10):
            self.move((i,))
        ans = 0
        for i in range(m, n+1):
            ans += self.patterns[i]
        return ans