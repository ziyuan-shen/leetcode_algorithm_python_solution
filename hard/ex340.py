class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        left = 0
        right = 1
        letterdic = {s[0]: 0}
        ans = 1
        while right < len(s):
            if s[right] in letterdic or len(letterdic) < k:
                letterdic[s[right]] = right
                right += 1
                ans = max(ans, right - left)
            else:
                left = min(list(letterdic.values()))
                letterdic.pop(s[left])
                left += 1
                letterdic[s[right]] = right
                right += 1
        return ans