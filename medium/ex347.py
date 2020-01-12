from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = [[count[num], num] for num in count]
        count.sort(reverse = True)
        return [t[1] for t in count[:k]]