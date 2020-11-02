from collections import defaultdict
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 1
        candy = [1 for _ in range(len(ratings))]
        count = defaultdict(int)
        for i in range(1, len(ratings)):
            if ratings[i] == ratings[i-1]:
                ans += 1
                count = defaultdict(int)
            elif ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
                ans += candy[i]
                count = defaultdict(int)
            else:
                if candy[i-1] > 1:
                    ans += 1
                else:
                    ans += count[1] + 2
                    candy[i-1] = 2
                for key in sorted(list(count.keys())):
                    if key != 1:
                        count[key-1] += count[key]
                        count.pop(key)
                count[candy[i-1] - candy[i]] += 1
        return ans