from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == None or t == None:
            return ""
        left, right = 0, 0
        t_dic = Counter(t)
        formed_num = 0
        required_num = len(t_dic)
        current_window = {}
        ans = float("Inf"), left, right
        while right < len(s):
            character = s[right]
            current_window[character] = current_window.get(character, 0) + 1
            if character in t_dic and t_dic[character] == current_window[character]:
                formed_num += 1
            while left <= right and formed_num == required_num:
                character = s[left]
                if right-left+1 < ans[0]:
                    ans = right-left+1, left, right
                current_window[character] -= 1
                if character in t_dic and t_dic[character] > current_window[character]:
                    formed_num -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("Inf") else s[ans[1]:ans[2]+1]
        