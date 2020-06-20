class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        patterndict = {1: {(idx+1,): l[:idx] + l[idx+1:] for idx in range(9)}}
        bridgedict = {(1, 3): 2, (4, 6): 5, (7, 9): 8, (1, 7): 4, (2, 8): 5, (3, 9): 6, (1, 9): 5, (3, 7): 5}
        for i in range(2, 10):
            patterndict[i] = {}
            for pre in patterndict[i-1]:
                for idx in range(len(patterndict[i-1][pre])):
                    num = patterndict[i-1][pre][idx]
                    if (pre[-1], num) in bridgedict:
                        if bridgedict[(pre[-1], num)] in pre:
                            patterndict[i][pre+(num,)] = patterndict[i-1][pre][:idx] + patterndict[i-1][pre][idx+1:]
                    elif (num, pre[-1]) in bridgedict:
                        if bridgedict[(num, pre[-1])] in pre:
                            patterndict[i][pre+(num,)] = patterndict[i-1][pre][:idx] + patterndict[i-1][pre][idx+1:]
                    else:
                        patterndict[i][pre+(num,)] = patterndict[i-1][pre][:idx] + patterndict[i-1][pre][idx+1:]
        ans = 0
        for i in range(m, n+1):
            ans += len(patterndict[i])
        return ans