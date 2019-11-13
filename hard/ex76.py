class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {char: -1 for char in t}
        idx = 0
        window = False
        left = None
        right = None
        while idx < len(s):
            while (not window) and idx < len(s):
                while left == None:
                    if s[idx] in t:
                        left = idx
                        dic[s[idx]] = idx
                    idx += 1
                if idx<len(s) and s[idx] in t:
                    dic[s[idx]] = max(dic[s[idx]], idx)
                window = True
                for m in dic.values():
                    if m == -1:
                        window = False
                idx += 1
            if not window:
                return ''
            if right == None:
                right = max(dic.values())
                min_window = s[left:right+1]
            if idx >= len(s):
                return min_window
            if s[idx] in dic:
                dic[s[idx]] = idx
                right = idx
                left = min(dic.values())
                if (right - left + 1) < len(min_window):
                    min_window = s[left:right+1]
            idx += 1
        return min_window
        
            
                    