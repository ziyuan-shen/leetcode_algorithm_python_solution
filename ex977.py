class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        self.ans = [elem ** 2 for elem in A]
        self.ans.sort()
        return self.ans
