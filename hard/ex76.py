class Solution:
    def minWindow(self, s: str, t: str) -> str:
        num_dic = {}
        for char in t:
            if char not in num_dic:
                num_dic[char] = 1
            else:
                num_dic[char] += 1
        count_dic = {char: 0 for char in t}
        idx_dic = {char: [] for char in t}
        idx = 0
        window = False
        left = None
        right = None
        while idx < len(s):
            while (not window) and idx < len(s):
                while idx < len(s) and left == None:
                    if s[idx] in num_dic:
                        left = idx
                        count_dic[s[idx]] = 1
                        idx_dic[s[idx]].append(idx)
                    idx += 1
                if idx<len(s) and s[idx] in num_dic:
                    if num_dic[s[idx]] == count_dic[s[idx]]:
                        idx_dic[s[idx]].pop(0)
                    else:
                        count_dic[s[idx]] += 1
                    idx_dic[s[idx]].append(idx)
                window = True
                for char in num_dic:
                    if num_dic[char] != count_dic[char]:
                        window = False
                idx += 1
            if not window:
                return ''
            if right == None:
                right = max(list(map(max, idx_dic.values())))
                left = min(list(map(min, idx_dic.values())))
                min_window = s[left:right+1]
            if idx >= len(s):
                return min_window
            if s[idx] in num_dic:
                idx_dic[s[idx]].pop(0)
                idx_dic[s[idx]].append(idx)
                right = idx
                left = min(list(map(min, idx_dic.values())))
                if (right - left + 1) < len(min_window):
                    min_window = s[left:right+1]
            idx += 1
        return min_window
        
            
                    