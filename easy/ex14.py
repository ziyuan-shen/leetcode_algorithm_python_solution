class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_str = ''
        if len(strs) == 0:
            return common_str
        min_length = min(map(len, strs))
        for i in range(min_length):
            letter = strs[0][i]
            tag = True
            for j in range(1, len(strs)):
                if strs[j][i] != letter:
                    tag = False
                    break
            if tag:
                common_str += letter
            else:
                break
        return common_str