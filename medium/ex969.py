class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        for i in range(len(A) - 1, -1, -1):
            if A[i] != i + 1:
                for j in range(i):
                    if A[j] == i + 1:
                        ans.append(j+1)
                        ans.append(i+1)
                        A = A[j::-1] + A[j+1:]
                        A = A[i::-1] + A[i+1:]
                        break
        return ans