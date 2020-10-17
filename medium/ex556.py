from bisect import bisect_right
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        if len(n) == 1:
            return -1
        for idx in range(len(n) - 2, -1, -1):
            if n[idx] < n[idx+1]:
                break
        if n[idx] >= n[idx+1]:
            return -1
        rem = list(n[idx+1:])
        rem.sort()
        replace = bisect_right(rem, n[idx])
        replace_num = rem[replace]
        rem[replace] = n[idx]
        ans = int(n[:idx] + replace_num + "".join(rem))
        if ans > 2 ** 31 - 1:
            return -1
        return ans