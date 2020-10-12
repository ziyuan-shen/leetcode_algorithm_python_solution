class Solution:
    def deleteChar(self, compressed, idx, rem, s):
        if idx == len(s):
            length = 0
            for c in compressed:
                if c[1] == 1:
                    length += 1
                else:
                    length += (1 + len(str(c[1])))
            self.ans = min(self.ans, length)
        elif rem == 0:
            compressed_copy = compressed.copy()
            if not compressed_copy:
                compressed_copy.append([s[idx], 1])
            idx += 1
            for i in range(idx, len(s)):
                if s[i] == compressed_copy[-1][0]:
                    compressed_copy[-1][1] += 1
                else:
                    compressed_copy.append([s[i], 1])
            idx = len(s)
            self.deleteChar(compressed_copy, idx, rem, s)
        else:
            self.deleteChar(compressed, idx + 1, rem - 1, s)
            if compressed and s[idx] == compressed[-1][0]:
                compressed[-1][1] += 1
                self.deleteChar(compressed, idx + 1, rem, s)
                compressed[-1][1] -= 1
            else:
                compressed.append([s[idx], 1])
                self.deleteChar(compressed, idx + 1, rem, s)
                compressed.pop()
        
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k == len(s):
            return 0
        self.ans = float("inf")
        self.deleteChar([], 0, k, s)
        return self.ans