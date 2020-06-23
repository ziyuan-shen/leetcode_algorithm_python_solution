from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        length = len(matrix)
        width = len(matrix[0])
        ps = [[0 for _ in range(width + 1)] for _ in range(length + 1)]
        for i in range(1, length+1):
            for j in range(1, width+1):
                ps[i][j] = matrix[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
        ans = 0
        print(ps)
        for r1 in range(1, length+1):
            for r2 in range(r1, length+1):
                dic = defaultdict(int)
                count = 0
                for c in range(width+1):
                    count += dic[ps[r2][c] - ps[r1-1][c] - target]
                    dic[ps[r2][c] - ps[r1-1][c]] += 1
                ans += count
        return ans