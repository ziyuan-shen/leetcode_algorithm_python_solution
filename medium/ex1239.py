class Solution:
    def search(self, current, idx, arr):
        if idx == len(arr):
            return len(current)
        s = arr[idx]
        for letter in s:
            if letter in current:
                return self.search(current, idx+1, arr)
        return max(self.search(current, idx+1, arr), self.search(current.union(set(s)), idx+1, arr))
    
    def maxLength(self, arr: List[str]) -> int:
        valid_arr = []
        for s in arr:
            if len(set(s)) == len(s):
                valid_arr.append(s)
        if not valid_arr:
            return 0
        return self.search(set(), 0, valid_arr)