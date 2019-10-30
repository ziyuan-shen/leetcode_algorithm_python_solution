class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(' ')
        return ' '.join(map(lambda x: x[::-1], l))
        