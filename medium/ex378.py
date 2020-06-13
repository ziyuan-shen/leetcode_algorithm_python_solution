class Solution:
    def merge(self, l1, l2):
        p1, p2 = 0, 0
        l = [0 for _ in range(len(l1) + len(l2) - 1)]
        idx = 0
        while idx < len(l):
            if l1[p1] <= l2[p2]:
                l[idx] = l1[p1]
                p1 += 1
            else:
                l[idx] = l2[p2]
                p2 += 1
            idx += 1
        return l
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 1:
            return matrix[0][k-1]
        matrix[0].append(float("inf"))
        l = matrix[0]
        for row in matrix[1:]:
            row.append(float("inf"))
            l = self.merge(l, row)
        return l[k-1]