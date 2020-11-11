class Solution:
    def enter(self, seq, s, n, k):
        for num in range(k):
            if len(seq) >= n-1 and seq[-(n-1):] + str(num) not in s:
                s.add(seq[-(n-1):] + str(num))
                res, newseq = self.enter(seq + str(num), s, n, k)
                if res:
                    return True, newseq
                s.remove(seq[-(n-1):] + str(num))
            elif len(seq) < n-1:
                res, newseq = self.enter(seq + str(num), s, n, k)
                if res:
                    return True, newseq
        if len(s) == self.total:
            return True, seq
        else:
            return False, ""
        
    def crackSafe(self, n: int, k: int) -> str:
        self.total = k ** n
        if n == 1:
            return "".join([str(i) for i in range(k)])
        s = set()
        res, seq = self.enter("0", s, n, k)
        return seq