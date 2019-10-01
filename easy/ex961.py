class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        temp = []
        for i in range(len(A)):
            if A[i] in temp:
                return A[i]
            else:
                temp.append(A[i])
