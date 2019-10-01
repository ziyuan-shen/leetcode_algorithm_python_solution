class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = [i for i in A if i % 2 == 0]
        odd  = [i for i in A if i % 2 == 1]
        return even + odd
