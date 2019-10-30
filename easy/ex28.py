class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        else:
            idx = 0
            while (idx+len(needle)) < len(haystack)+1:
                if haystack[idx:idx+len(needle)] == needle:
                    return idx
                else:
                    idx += 1
            return -1
        