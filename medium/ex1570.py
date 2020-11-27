class SparseVector:
    def __init__(self, nums: List[int]):
        self.idxset = set()
        self.values = dict()
        for i in range(len(nums)):
            if nums[i] != 0:
                self.idxset.add(i)
                self.values[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        idx = self.idxset.intersection(vec.idxset)
        for i in idx:
            ans += (self.values[i] * vec.values[i])
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)