from collections import defaultdict

class Solution:
    def check(self, s, k):
        dic = defaultdict(list)
        for idx, letter in enumerate(s):
            dic[letter].append(idx)
        flag = True
        for letter in dic:
            if len(dic[letter]) < k:
                flag = False
                for idx in dic[letter]:
                    s[idx] = "#"
        if flag:
            return len(s)
        idx = 0
        substrings = []
        start = 0
        while idx < len(s):
            if s[idx] == "#":
                start = idx + 1
            elif idx == len(s) - 1 or s[idx+1] == "#":
                substrings.append(s[start:idx+1])
            idx += 1
        ans = 0
        for substring in substrings:
            ans = max(self.check(substring, k), ans)
        return ans
        
    def longestSubstring(self, s: str, k: int) -> int:
        return self.check(list(s), k)
        