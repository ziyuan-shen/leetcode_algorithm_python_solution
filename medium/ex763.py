class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = [[0, {S[0]}]]
        for idx in range(1, len(S)):
            flag = True
            for i in range(len(ans)):
                if S[idx] in ans[i][1]:
                    new_set = ans[i][1]
                    for j in range(i+1, len(ans)):
                        new_set = new_set.union(ans[j][1])
                    ans[i][1] = new_set
                    ans[i][0] = idx
                    del ans[i+1:]
                    flag = False
                    break
            if flag:
                ans.append([idx, {S[idx]}])
        ans = [x[0] for x in ans]
        ans = [-1] + ans
        ans = [ans[i] - ans[i-1] for i in range(1, len(ans))]
        return ans