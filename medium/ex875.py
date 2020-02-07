class Solution:
    def isPossible(self, piles, H, K):
        return sum([(pile - 1) // K + 1 for pile in piles]) <= H
    
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        piles.sort()
        low = 1
        high = piles[-1]
        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(piles, H, mid):
                if mid == low or not self.isPossible(piles, H, mid - 1):
                    return mid
                high = mid - 1
            else:
                low = mid + 1
                