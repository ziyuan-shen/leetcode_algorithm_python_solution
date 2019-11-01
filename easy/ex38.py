class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        pre_seq = self.countAndSay(n-1)
        seq = ''
        start_idx = 0
        end_idx = 0
        while start_idx < len(pre_seq):
            while end_idx < len(pre_seq) and pre_seq[end_idx] == pre_seq[start_idx]:
                end_idx += 1
            seq += str(end_idx - start_idx)
            seq += pre_seq[start_idx]
            start_idx = end_idx
        return seq