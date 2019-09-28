class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        high = len(A) - 1
        low = 0
        mid = (low + high) // 2
        while True:
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] >= A[mid-1]:
                low = mid
                mid = (low + high) // 2
            else:
                high = mid
                mid = (low + high) // 2