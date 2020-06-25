class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        removable_indices = set()
        idx = 0
        while idx < len(S) - 2:
            if S[idx] == S[idx+1] and S[idx] == S[idx+2]:
                letter = S[idx]
                removable_indices.add(idx+1)
                removable_indices.add(idx+2)
                idx += 3
                while idx < len(S) and S[idx] == letter:
                    removable_indices.add(idx)
                    idx += 1
            else:
                idx += 1
        ans = 0
        for word in words:
            p1, p2 = 0, 0
            while p1 < len(S) and p2 < len(word):
                if S[p1] == word[p2]:
                    p1 += 1
                    p2 += 1
                elif p1 not in removable_indices:
                    break
                else:
                    p1 += 1
            if p2 == len(word):
                for idx in range(p1, len(S)):
                    if idx not in removable_indices:
                        ans -= 1
                        break
                ans += 1
        return ans