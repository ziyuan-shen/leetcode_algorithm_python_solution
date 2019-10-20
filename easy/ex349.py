class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            if i in nums2 and i not in l:
                l.append(i)
        return l