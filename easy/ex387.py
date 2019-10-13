class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        count_dic = {}
        for i in range(len(s)):
            if s[i] in count_dic:
                count_dic[s[i]] += 1
            else:
                count_dic[s[i]] = 1
        for ch in count_dic:
            if count_dic[ch] == 1:
                return s.index(ch)
        return -1