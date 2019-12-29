class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in ans:
                ans[word_sorted] = [word]
            else:
                ans[word_sorted].append(word)
        return ans.values()