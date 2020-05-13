class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        length = len(M)
        width = len(M[0])
        ans = [[0 for _ in range(width)] for _ in range(length)]
        for i in range(length):
            for j in range(width):
                acc = 0
                count = 0
                for cell in [(i, j), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                    if cell[0] >= 0 and cell[0] < length and cell[1] >= 0 and cell[1] < width:
                        count += 1
                        acc += M[cell[0]][cell[1]]
                ans[i][j] = acc // count
        return ans