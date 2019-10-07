class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            idx = m + i
            while nums2[i] < nums1[idx-1] and idx>=1:
                nums1[idx] = nums1[idx-1]
                idx -= 1
            nums1[idx] = nums2[i]
        return nums1