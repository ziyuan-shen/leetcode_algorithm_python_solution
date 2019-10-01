class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for i in arr:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 0
        if len(counter) == len(set(list(counter.values()))):
            return True
        else:
            return False