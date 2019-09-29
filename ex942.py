class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = []
        low = 0
        high = len(S)
        for i in range(len(S)):
            if S[i]=='I':
                l.append(low)
                low += 1
            else:
                l.append(high)
                high -= 1
        l.append(low)
        return l