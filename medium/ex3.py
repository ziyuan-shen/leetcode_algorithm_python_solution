class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct_substring = []
        idx = 0
        max_length = 0
        while idx<len(s):
            while idx<len(s) and (s[idx] not in distinct_substring):
                distinct_substring.append(s[idx])
                if len(distinct_substring) > max_length:
                    max_length = len(distinct_substring)
                idx += 1
            if idx<len(s):
                char = s[idx]
                distinct_substring = []
                idx -= 1
                while s[idx] != char:
                    idx -= 1
                idx += 1
        return max_length