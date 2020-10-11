class Solution:
    mem = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 == s2
        for i in range(1, len(s1)):
            if (s1[:i], s2[:i]) not in self.mem:
                self.mem[(s1[:i], s2[:i])] = self.isScramble(s1[:i], s2[:i])
            a = self.mem[(s1[:i], s2[:i])]
            if (s1[i:], s2[i:]) not in self.mem:
                self.mem[(s1[i:], s2[i:])] = self.isScramble(s1[i:], s2[i:])
            b = self.mem[(s1[i:], s2[i:])]
            if (s1[:i], s2[-i:]) not in self.mem:
               self.mem[(s1[:i], s2[-i:])] = self.isScramble(s1[:i], s2[-i:])
            c = self.mem[(s1[:i], s2[-i:])]
            if (s1[i:], s2[:-i]) not in self.mem:
                self.mem[(s1[i:], s2[:-i])] = self.isScramble(s1[i:], s2[:-i])
            d = self.mem[(s1[i:], s2[:-i])]
            if (a and b) or (c and d):
                return True
        return False