class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = dict()
        for num in arr:
            target = (k - num % k) % k
            if target in d:
                d[target] -= 1
                if d[target] == 0:
                    d.pop(target)
            else:
                if num % k in d:
                    d[num % k] += 1
                else:
                    d[num % k] = 1
        return len(d) == 0