class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        possible = {}
        for size in range(minSize, maxSize + 1):
            for i in range(len(s) - size + 1):
                if s[i:i+size] in possible:
                    possible[s[i:i+size]] += 1
                elif len(set(s[i:i+size])) <= maxLetters:
                    possible[s[i:i+size]] = 1
        return max(possible.values()) if possible else 0