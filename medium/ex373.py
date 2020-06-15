class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pairs.append([nums1[i] + nums2[j], nums1[i], nums2[j]])
        pairs.sort()
        pairs = pairs[:k]
        return [pair[1:] for pair in pairs]