from operator import truediv, mul, add, sub
from collections import deque
class Solution(object):
    def permutations(self, li):
        q = deque([([li[i]], li[:i] + li[i+1:]) for i in range(len(li))])
        while True:
            l1, l2 = q.popleft()
            if not l2:
                q.appendleft((l1, l2))
                break
            for i in range(len(l2)):
                q.append((l1 + [l2[i]], l2[:i] + l2[i+1:]))
        return [t[0] for t in q]
    
    def judgePoint24(self, A):
        perms = self.permutations(A)
        ops = [add, sub, mul, truediv]
        first = set()
        for perm in perms:
            num1 = perm.pop(0)
            num2 = perm.pop(1)
            if (num1, num2) not in first:
                first.add((num1, num2))
                for op1 in ops:
                    if not (op1 == truediv and num2 == 0):
                        perms2 = self.permutations(perm + [op1(num1, num2)]) 
                        for perm2 in perms2:
                            num3 = perm2.pop(0)
                            num4 = perm2.pop(0)
                            for op2 in ops:
                                if not (op2 == truediv and num4 == 0):
                                    perms3 = self.permutations(perm2 + [op2(num3, num4)])
                                    for perm3 in perms3:
                                        for op3 in ops:
                                            if not(op3 == truediv and perm3[1] == 0):
                                                ans = op3(perm3[0], perm3[1])
                                                if abs(ans - 24) < 1e-6:
                                                    return True
        return False