class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        s = set()
        s.add(tuple(cells))
        l = [tuple(cells)]
        rep = 0
        while True:
            prev = l[-1]
            next_tuple = (0,)
            for i in range(1, 7):
                if prev[i-1] == prev[i+1]:
                    next_tuple += (1,)
                else:
                    next_tuple += (0,)
            next_tuple += (0,)
            if next_tuple in s:
                rep = l.index(next_tuple)
                break
            else:
                l.append(next_tuple)
                s.add(next_tuple)
        if N < len(l):
            return l[N]
        else:
            repnum = len(l) - rep
            remainder = (N - len(l) + 1) % repnum
            if remainder == 0:
                return l[-1]
            else:
                return l[rep + remainder - 1]