class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n != 0:
            n, m = n // 26, n % 26
            if m > 0:
                title = chr(64+m) + title
            else:
                title = 'Z' + title
                n -= 1
        return title