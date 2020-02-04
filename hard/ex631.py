class Excel:

    def __init__(self, H: int, W: str):
        self.nrow = H
        self.ncol = ord(W) - 64
        self.data = [[0 for _ in range(self.ncol)] for _ in range(self.nrow)]
        self.sumfomula = {}

    def set(self, r: int, c: str, v: int) -> None:
        self.data[r-1][ord(c) - 65] = v
        if (r, c) in self.sumfomula:
            self.sumfomula.pop((r, c))
        update_flag = True
        while update_flag:
            update_flag = False
            for coord, strs in self.sumfomula.items():
                prev = self.get(coord[0], coord[1])
                new = self.sum(coord[0], coord[1], strs)
                if new != prev:
                    update_flag = True

    def get(self, r: int, c: str) -> int:
        return self.data[r-1][ord(c) - 65]
    
    def sumMatrix(self, r1, c1, r2, c2):
        ans = 0
        for r in range(r1-1, r2):
            ans += sum(self.data[r][ord(c1) - 65:ord(c2) - 64])
        return ans

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.sumfomula[r, c] = strs
        ans = 0
        for elem in strs:
            if len(elem) <= 3:
                ans += self.get(int(elem[1:]), elem[0])
            else:
                topl = elem.split(":")[0]
                bottomr = elem.split(":")[1]
                ans += self.sumMatrix(int(topl[1:]), topl[0], int(bottomr[1:]), bottomr[0])
        self.data[r-1][ord(c) - 65] = ans
        return ans

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)