class Solution:
    mem = {}
    def deleteChar(self, compressed, idx, rem, s):
        if rem == 0 or idx == len(s):
            compressed_copy = compressed.copy()
            if compressed_copy:
                while idx < len(s) and s[idx] == compressed_copy[-1][0]:
                    compressed_copy[-1][1] += 1
                    idx += 1
            length = 0
            for c in compressed_copy:
                if c[1] == 1:
                    length += 1
                else:
                    length += (1 + len(str(c[1])))
            if idx not in self.mem:
                com = []
                l = 0
                for char in s[idx:]:
                    if com and char == com[-1][0]:
                        com[-1][1] += 1
                    else:
                        com.append([char, 1])
                for c in com:
                    if c[1] == 1:
                        l += 1
                    else:
                        l += (1 + len(str(c[1])))
                self.mem[idx] = l
            self.ans = min(self.ans, length + self.mem[idx])
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
        
    def getLengthOfOptimalCompression(self, s, k):
        if k == len(s):
            return 0
        self.ans = float("inf")
        self.deleteChar([], 0, k, s)
        return self.ans

s = Solution()
print(s.getLengthOfOptimalCompression("aabbaa", 2))