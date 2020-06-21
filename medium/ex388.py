class Solution:
    def getLength(self, lines):
        if not lines:
            return 0
        directories = {lines[0]: []}
        current = lines[0]
        for line in lines[1:]:
            if line[0] != "\t":
                directories[line] = []
                current = line
            else:
                directories[current].append(line[1:])
        print(directories)
        ans = 0
        for direc in directories:
            if "." in direc:
                ans = max(ans, len(direc))
            else:
                sublength = self.getLength(directories[direc])
                if sublength != 0:
                    ans = max(ans, len(direc) + 1 + sublength)
        return ans
        
    def lengthLongestPath(self, input: str) -> int:
        if not input:
            return 0
        lines = input.split("\n")
        return self.getLength(lines)