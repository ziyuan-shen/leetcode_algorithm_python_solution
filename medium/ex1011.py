class Solution:
    def eval(self, weights, D, capacity):
        current_d = 1
        current_weight = 0
        for weight in weights:
            if weight > capacity:
                return False
            elif current_weight + weight > capacity:
                current_weight = weight
                current_d += 1
            else:
                current_weight += weight
        return current_d <= D
        
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        acc = sum(weights)
        lower = acc // D
        if acc % D != 0:
            lower += 1
        if len(weights) <= D:
            return max(weights)
        group = len(weights) // D
        if len(weights) % D != 0:
            group += 1
        idx = 0
        upper = 0
        while idx < len(weights):
            upper = max(upper, sum(weights[idx:idx+group]))
            idx += group
        while lower <= upper:
            mid = (lower + upper) // 2
            if not self.eval(weights, D, mid):
                lower = mid + 1
            elif mid == lower or not self.eval(weights, D, mid - 1):
                return mid
            else:
                upper = mid - 1
        